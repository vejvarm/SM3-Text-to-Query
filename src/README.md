# Source Directory 

This directory contains code for the reproduction of the experiments. 

Below you will find a description of the subdirectories.


- `./src/setup_dbs` contains the code to set up the four different database systems (PostgreSQL, GraphDB, Neo4j, and MongoDB) and populate them with Synthea data.
- `./src/run_experiments` contains the code to
  replicate our experiments for all database models, LLMs, prompts, and few-shot
  sampling (repetitions).
- `./src/evaluation` contains the code to evaluate the
  results obtained by the LLMs for our four databases, including the necessary
  data-cleaning logic. It computes Execution Accuracy (EA) and Valid Efficiency
  Score (VES) for each combination of LLM, database model, and prompt-setting.