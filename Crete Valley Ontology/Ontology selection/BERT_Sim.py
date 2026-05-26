import numpy as np
import torch
import pandas as pd
import os
import sys
from owlready2 import get_ontology
from rdflib import *
from rdflib.namespace import split_uri
from wordembedding import Energy_Bert


# Get all the class names of an ontology
def get_ontoclass(path):
    lst = []
    if path.endswith('.ttl'):
        g = Graph()
        g.parse(path)
        lst = []
        for s, p, o in g.triples((None, RDF.type, OWL.Class)):
            if isinstance(s, URIRef):
                class_name = split_uri(s)[-1]
                lst.append(class_name)
    else:
        onto = get_ontology(path).load()
        for i in list(onto.classes()):
            class_name = str(i).split('.')[-1]
            lst.append(class_name)
    return lst


def get_bertsim(path, sim_min=0.6):
    print("Ontology file name:", os.path.basename(path))
    nodes_lst = get_ontoclass(path)
    print('The classes of ontology_nodes:', nodes_lst)
    print('Number of classes:', len(nodes_lst))

    word_chain = ['Building', 'Angle', 'Date', 'Time','Coal','Weather', 'PV', 'Cooling', 'Heating', 'Storage', 'Pressure', 'Temperature', 'Humidity',
                  'WPP', 'EnergyManagement', 'Measurement', 'solar', 'EnergyDemand', 'Electricity', 'Hydrogen', 'geothermal', 'Sensor', 'EnergyMeter'
                  'EnergyConsumption', 'Energy', 'RenewableEnergyResources', 'consumers', 'CIM', 'IEC61970', 'MW', 'kW', 'Voltage', 'Power', 'Service', 'Current', 'Water', 
                  'Frequency', 'Magnitude'] #word chain from CQs

    bert = Energy_Bert()
    sim_tensor = bert.sim(nodes_lst, word_chain)

    threshold = sim_tensor > sim_min
    sum_bert = sim_tensor[threshold].sum().item()

    print(f'BERT similarity is:', sum_bert)

    return round(sum_bert, 3)


if __name__ == '__main__':
    threshold_range = np.arange(0.4, 0.91, 0.05)
    print('Sim_threshold chosen:', threshold_range)
    for sim_threshold in threshold_range:
        sim_threshold = round(sim_threshold, 2)
        print("Similarity threshold value:", sim_threshold)
        sim_list = [get_bertsim("../Ontologies/oeo.owl", sim_threshold),
                    get_bertsim("Ontologies/saref4bldg.ttl", sim_threshold),
                    get_bertsim("Ontologies/saref4ener.ttl", sim_threshold),
                    get_bertsim("Ontologies/saref4grid.ttl", sim_threshold),
                    get_bertsim("Ontologies/SARGON.ttl", sim_threshold),
                    get_bertsim("Ontologies/sbeo.ttl", sim_threshold),
                    get_bertsim("Ontologies/SSN.ttl", sim_threshold),
                    get_bertsim("Ontologies/TheCimOntology.ttl", sim_threshold),
                    get_bertsim("Ontologies/em-kpi.ttl", sim_threshold),
                    get_bertsim("Ontologies/fso.ttl", sim_threshold)]
        onto_list = ['SAREF4BLDG', 'SAREF4ENER', 'SAREF4GRID', 'SARGON', 'SBEO',  'SSN',  'CIM', 'EM-KPI',
                     'FSO', ]
        if len(onto_list) != len(sim_list):
            min_length = min(len(onto_list), len(sim_list))
            onto_list = onto_list[:min_length]
            sim_list = sim_list[:min_length]
        df = pd.DataFrame({'Ontology': onto_list, 'BERT_Sim': sim_list})
        df.to_csv(f'./Results/BERTSIMforOntologySelection_{sim_threshold}.csv')
