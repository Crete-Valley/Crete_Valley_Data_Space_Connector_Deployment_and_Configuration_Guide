import os
from rdflib import Graph, RDF, RDFS, OWL

def count_owl_classes(owl_file):
    # Load the OWL file
    g = Graph()
    g.parse(owl_file, format='xml')

    # Count the number of OWL classes
    classes = set()
    for s, p, o in g.triples((None, RDF.type, OWL.Class)):
        classes.add(s)
    for s, p, o in g.triples((None, RDF.type, RDFS.Class)):
        classes.add(s)

    # Extract class names
    class_names = [str(cls).split('/')[-1].split('#')[-1].lower() for cls in classes]

    return len(classes), class_names

def count_cim_folders(cim_directory):
    # Count the number of folders in the CIM directory
    folders = [name for name in os.listdir(cim_directory) if os.path.isdir(os.path.join(cim_directory, name))]
    return len(folders), folders

def find_matches(owl_classes, cim_folders):
    # Find matches between OWL classes and CIM folders
    matches = set(owl_classes) & set(cim_folders)
    return matches

def main():
    owl_file = '../../sargon/Resources/Ontology-files/SARGON.owl'
    cim_directory = '../../dataModel.EnergyCIM'

    num_owl_classes, owl_classes = count_owl_classes(owl_file)
    num_cim_folders, cim_folders = count_cim_folders(cim_directory)
    matches = find_matches(owl_classes, cim_folders)

    print(f"Number of OWL classes: {num_owl_classes}")
    print(f"Number of CIM folders: {num_cim_folders}")
    print(f"Number of matches between OWL classes and CIM folders: {len(matches)}")
    print("Matches between OWL classes and CIM folders:")
    #for match in matches:
        #print(match)

if __name__ == "__main__":
    main()
