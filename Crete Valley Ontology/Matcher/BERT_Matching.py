import os
import pandas as pd
from owlready2 import get_ontology
from wordembedding import Energy_Bert


class Ontology:
    def __init__(self, path):
        self.path = path

    @property
    def name(self):
        return os.path.basename(self.path).split('.')[0]

    def onto(self):
        return get_ontology(self.path).load()

    def get_classes(self):
        class_list = []
        for i in list(self.onto().classes()):
            class_name = str(i).split('.')[-1]
            class_list.append(class_name)
        return class_list

    def get_data_properties(self):
        data_property_list = []
        for i in list(self.onto().data_properties()):
            data_property_name = str(i).split('.')[-1]
            data_property_list.append(data_property_name)
        return data_property_list

    def get_object_properties(self):
        object_property_list = []
        for i in list(self.onto().object_properties()):
            object_property_name = str(i).split('.')[-1]
            object_property_list.append(object_property_name)
        return object_property_list


def bert_matching(list1, list2, sim_threshold=0.8):
    bert = Energy_Bert()

    onto1_list = []
    onto2_list = []
    sim_list = []

    sim_tensor = bert.sim(list1, list2)
    for i in range(sim_tensor.shape[0]):
        for j in range(sim_tensor.shape[1]):
            sim = sim_tensor[i][j]
            if sim_tensor[i][j] > sim_threshold:
                onto1_list.append(list1[i])
                onto2_list.append(list2[j])
                sim_list.append(round(sim.item(), 3))

    return onto1_list, onto2_list, sim_list


def class_matching(onto1, onto2):
    onto1_classes = onto1.get_classes()
    onto2_classes = onto2.get_classes()
    print(f'classes of {onto1.name}', onto1_classes)
    print(f'classes of {onto2.name}', onto2_classes)
    onto1_lst, onto2_lst, sim_lst = bert_matching(onto1_classes, onto2_classes)
    df = pd.DataFrame({'Classes'})
    df.to_csv(f'./Results/Matching_Results_{onto1.name}_and_{onto2.name}.csv',
              mode='a', header=False, index=False)
    df = pd.DataFrame({f'{onto1.name}': onto1_lst, f'{onto2.name}': onto2_lst, 'BERT_Sim': sim_lst})
    df.to_csv(f'./Results/Matching_Results_{onto1.name}_and_{onto2.name}.csv',
              mode='a', header=False, index=False)


def data_property_matching(onto1, onto2):
    onto1_data_properties = onto1.get_data_properties()
    onto2_data_properties = onto2.get_data_properties()
    print(f'data_properties of {onto1.name}', onto1_data_properties)
    print(f'data_properties of {onto2.name}', onto2_data_properties)
    onto1_lst, onto2_lst, sim_lst = bert_matching(onto1_data_properties, onto2_data_properties)
    df = pd.DataFrame({'Data Properties'})
    df.to_csv(f'./Results/Matching_Results_{onto1.name}_and_{onto2.name}.csv',
              mode='a', header=False, index=False)
    df = pd.DataFrame({f'{onto1.name}': onto1_lst, f'{onto2.name}': onto2_lst, 'BERT_Sim': sim_lst})
    df.to_csv(f'./Results/Matching_Results_{onto1.name}_and_{onto2.name}.csv',
              mode='a', header=False, index=False)


def object_property_matching(onto1, onto2):
    onto1_object_properties = onto1.get_object_properties()
    onto2_object_properties = onto2.get_object_properties()
    print(f'object_properties of {onto1.name}', onto1_object_properties)
    print(f'object_properties of {onto2.name}', onto2_object_properties)
    onto1_lst, onto2_lst, sim_lst = bert_matching(onto1.get_object_properties(), onto2.get_object_properties())
    df = pd.DataFrame({'Object Properties'})
    df.to_csv(f'./Results/Matching_Results_{onto1.name}_and_{onto2.name}.csv',
              mode='a', header=False, index=False)
    df = pd.DataFrame({f'{onto1.name}': onto1_lst, f'{onto2.name}': onto2_lst, 'BERT_Sim': sim_lst})
    df.to_csv(f'./Results/Matching_Results_{onto1.name}_and_{onto2.name}.csv',
              mode='a', header=False, index=False)


def onto_matching(onto1, onto2):
    print(f'Matching between {onto1.name} and {onto2.name}')
    class_matching(onto1, onto2)
    object_property_matching(onto1, onto2)
    data_property_matching(onto1, onto2)


if __name__ == '__main__':
    sargon = Ontology('../ontology merging/sargonandcim.owl')
    iec_cim = Ontology('../ontologies/em-kpi.rdf')

    onto_matching(sargon, iec_cim)
