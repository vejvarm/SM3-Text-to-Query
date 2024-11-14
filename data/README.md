# Data Directory

The following directory contains a variety of data used in the SM3-Text-to-Query project. 

Below you will find a brief description of the specific subdirectories.


- `./synthea_database` contains the Synthea data used as the basis for PostgreSQL, Graph DB (RDF), Neo4j, and MongoDB.
- `./dataset/train_dev`contains the annotated
  train and dev splits for all four query languages: SQL, SPARQL, Cypher, and
  MQL
- `./dataset/processed_data` contains different data splits, including the responses from the respective databases.
- `./dataset/question_templates` contains the 408 question templates used to construct SM3-Text-to-Query.
- `./results` contains the results for each of the
  evaluated database systems and query languages for each of the five prompts,
the four LLMs for dev (results on test are not published to not expose the questions)
