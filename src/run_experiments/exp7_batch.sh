#!/bin/bash

# Define arrays for your parameters
datasets=("test" "dev")
query_languages=("sql" "mql" "cypher" "sparql1" "sparql2")

# Loop through each dataset
for dataset in "${datasets[@]}"; do
  # Loop through each query language
  for query_language in "${query_languages[@]}"; do
    # Construct and run the command
    python run_llm_exp7.py --llm_models gpt-3.5-turbo-0125-batch --datasets "$dataset" --query_languages "$query_language" --bm25_shots 5
    # display the success message
    echo "Success: $dataset on $query_language"
  done
done
