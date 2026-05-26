# Ontology Development Framework

The development of SARGON2 ontology in this work utilizes the framework developed in Pan et al. (2023)

1. [Domain and Scope Determination](#domain-and-scope-determination)
2. [Requirement Specification](#requirement-specification)
3. [Knowledge Search](#knowledge-search)
4. [Ontology Selection](#ontology-selection)
5. [Ontology Matching](#ontology-matching)
6. [Ontology Merging](#ontology-merging)
7. [Conceptualization](#conceptualization)
8. [Evaluation](#evaluation)

---

## Domain and Scope Determination 
The first step in ontology development is to clearly define its purpose, target users, use cases, and requirements. Following the guidelines in the Ontology Requirement Specification Document (ORSD), we focus on domains such as energy, building, weather, and Earth Observation (EO) information.

## Requirement Specification 
The ORSD outlines two types of ontology requirements:
- **Non-functional Requirements:** General criteria the ontology must meet.
- **Functional Requirements:** Specific content-based needs, expressed as competency questions (CQs) along with their answers.

The final section of the ORSD highlights the frequency of terms (nouns, adjectives, verbs) from CQs that will be formally represented in the ontology through entities, classes, attributes, relations, and instances.

## Knowledge Search 
This phase involves identifying existing ontologies and data models relevant to our domain using keywords from the ORSD, such as *Energy*, *Building*, *Weather*, and *Renewable Energy Resources*. The search is conducted using tools like Terminology Service NFDI4ING, LOV, and FIWARE.

### Knowledge Search Results
| Ontology                    | Domain                             |
|-----------------------------|------------------------------------|
| SARGON                      | Energy, Building, Device           |
| SAREF4BLDG                 | Energy, Building                   |
| SAREF4ENER                  | Energy                             |
| SAREF4GRID                  | Energy, Smart Grid                 |
| EM-KPI ontology             | Energy, Building, Device, Weather  |
| Semantic Sensor Network      | Device                             |
| Flow Systems Ontology        | Energy                             |
| CIM Ontology                | Energy                             |
| Smart Building Evacuation    | Building                           |

## Ontology Selection 
To ensure alignment with the ORSD while developing SARGON2 (an extension of SARGON), suitable ontologies are selected based on semantic similarity scores calculated using Energy BERT—a model tailored for energy-related contexts.

## Ontology Matching 
This step involves analyzing semantic correspondences between selected ontologies to identify overlapping classes or properties before merging. The process uses a pre-trained Energy BERT model to assess similarity scores.

## Ontology Merging 
Merging combines two or more ontologies into a single, cohesive structure. Protégé software is used to integrate ontologies like SARGON and CIM effectively.

## Conceptualization 
After merging, adjustments are made to better align with the requirement specifications. New concepts such as *Hydrogen*, *Biomass*, *Biogas*, and *Geothermal* are defined to ensure comprehensive coverage of CQs.

## Evaluation 
SARGON2 is evaluated using tools like OOPS and the Pellet reasoner plugin within Protégé to assess its performance and reliability.


## Reference
Zhiyu Pan, Yuting Gao, Ferdinanda Ponci, and Antonello Monti. 2023. Semi-Automatic Ontology Development Framework for Building Energy Data Management. IEEE Access 11 (2023), 111991–112003. doi:10.1109/ACCESS.2023.3323335
---