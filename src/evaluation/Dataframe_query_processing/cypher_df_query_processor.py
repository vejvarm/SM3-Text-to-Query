import pandas as pd
from neo4j import GraphDatabase
import os
import time

# Neo4j credentials and connection URI
uri = "bolt://localhost:7687"  # Update with your Neo4j URI
user = "neo4j"  # Update with your Neo4j username
password = "password"  # Update with your Neo4j password

def execute_cypher_query(query, uri, user, password):
    start_time = time.time()
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        result = session.run(query)
        records = [record.data() for record in result]
    driver.close()
    end_time = time.time()
    execution_time = end_time - start_time
    return records, execution_time

def add_cypher_results_columns(df, columns, uri, user, password, start_index=0, output_file=None):
    for index in range(start_index, len(df)):
        for column in columns:
            query = str(df.at[index, column])
            print(f"Processing index {index} for column {column}, query: {query}")
            try:
                cypher_results, exec_time = execute_cypher_query(query, uri, user, password)
                df.at[index, f'{column}_results'] = cypher_results
                df.at[index, f'{column}_query_time'] = exec_time
            except Exception as e:
                print(f"Error occurred for index {index} in column {column}: {e}")
                df.at[index, f'{column}_results'] = None
                df.at[index, f'{column}_query_time'] = None

        if output_file:
            df.to_csv(output_file, index=False)
            print(f"Saved progress to {output_file}")

    return df

def process_dataframe_cypher(df, uri, user, password):
    # Add SPARQL results for 'cypher' column
    df = add_cypher_results_columns(df, ['cypher'], uri, user, password)
    return df

def process_dataframe_cypher_llm(df, uri, user, password, output_file=None, start_index=0):
    # Add Cypher results for both 'cypher_llm' and 'cypher_llm_processed' columns
    df = add_cypher_results_columns(df, ['cypher_llm_processed'], uri, user, password, start_index=start_index, output_file=output_file)
    return df

if __name__ == "__main__":
    # Example how to use the functions
    
    # Neo4j credentials and connection URI
    uri = "bolt://localhost:7687"  # Update with your Neo4j URI
    user = "neo4j"  # Update with your Neo4j username
    password = "password"  # Update with your Neo4j password

    input_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/python/modules/LLM_output_sparql/QA_sparql_prompt_schema_fewshots_gemini.csv")
    # Process the Dataframe
    processed_df = process_dataframe_cypher(input_df, uri, user, password)
    print(processed_df)

    train_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/solutions/train.csv")
    # Process the Dataframe
    processed_df = process_dataframe_cypher_llm(train_df, uri, user, password)
    print(processed_df)