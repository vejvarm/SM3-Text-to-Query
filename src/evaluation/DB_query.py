import pandas as pd
import psycopg2
import re
import glob
import os
from Dataframe_query_processing.cypher_df_query_processor import process_dataframe_cypher_llm
from Dataframe_query_processing.sparql_df_query_processor import process_dataframe_sparql_llm
from Dataframe_query_processing.sql_df_query_processor import process_dataframe_sql_llm
from Dataframe_query_processing.mql_df_query_processor import process_dataframe_mql_llm

from psycopg2 import pool
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# Load additional datasets for comparison
test = pd.read_csv("test.csv")
dev = pd.read_csv("dev.csv")
sample_dev = pd.read_csv("sample_dev.csv")
sample_test = pd.read_csv("sample_test.csv")

# Database credentials and connection URIs
neo4j_uri = "bolt://localhost:7687"  # Update with your Neo4j URI
neo4j_user = "neo4j"  # Update with your Neo4j username
neo4j_password = "password"  # Update with your Neo4j password

graphdb_url = "http://160.85.252.225:7200/repositories/Synthea3"  # Update with your GraphDB URL
graphdb_user = "admin"  # Update with your GraphDB username
graphdb_password = "root"  # Update with your GraphDB password

# Establish Postgres connection
connection = psycopg2.pool.SimpleConnectionPool(
    1,
    5,
    dbname="postgres",
    user="postgres",  # Update with your Postgres username
    password="postgres",  # Update with your Postgres password
    host="localhost",  # Update with your Postgres hostname
    port="5432"  # Update with your Postgres port
)

# Function to extract Cypher queries
def extract_cypher_query(text):
    if isinstance(text, str):
        # Das Muster berücksichtigt sowohl das Semikolon als auch den [Q] Lookahead
        pattern = r'MATCH.*?(;|(?=\[Q\]))'
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            matched_text = match.group(0).replace('\n', ' ').strip()
            # Wenn das Muster vor [Q] endet, das abschließende [Q] entfernen
            if matched_text.endswith('Q'):
                matched_text = matched_text[:-2].strip()
            return matched_text
        return text.strip()  # Wenn keine Übereinstimmung gefunden wird, den ursprünglichen Text zurückgeben
    else:
        return ''

# Function to extract SPARQL queries
def extract_sparql_query(text):
    if isinstance(text, str):
        pattern = r'PREFIX.*?SELECT.*?WHERE\s*\{.*?\}'
        match = re.search(pattern, text, re.DOTALL)
        return match.group(0).replace('\n', ' ') if match else ''
    else:
        return ''

# Function to extract SQL queries
def extract_sql_queries(text):
    if isinstance(text, str):
        # Pattern to match SQL queries that end with ; or [Q]
        pattern = r'SELECT.*?;|SELECT.*?(?=\[Q\])'
        
        # Find the first match in the text
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        
        # If there is a match, process it
        if match:
            matched_query = match.group(0).strip().replace('\n', ' ')
            return matched_query
        else:
            # If no match, return the original text
            return text.strip()
    else:
        return ''
        
        
        
import re

def extract_mongodb_query(string):
    if "No answer possible based on given input" in string:
        return "No answer possible based on given input"

    # Extract the MongoDB query using a regular expression
    match = re.search(r"(db\.\w+\.[^;]+)", string)
        
    # Remove the '[MongoDB]' prefix if present
    string = string.replace("[MongoDB]", "").strip()
    string = string.replace("[MQL]:", "")
    string = string.replace(";", "")
    string = string.replace("```python", "")
    string = string.replace("mongodb", "")
    string = string.replace("```json", "")
    string = string.replace("```", "")
    string = string.strip()
    

    # Extract the MongoDB query using a regular expression
    match = re.search(r"(db\.\w+\.[^;]+)", string)

    if match:
        query = match.group(1)
        
        # Remove any trailing semicolon and whitespace
        query = query.rstrip(";").strip()
        
        return query
    else:
        return string

# Automatically retrieve input directories
input_dirs = [d for d in os.listdir() if os.path.isdir(d) and d.startswith("LLM_output_")]
file_paths = [file_path for input_dir in input_dirs for file_path in glob.glob(input_dir + r"/*.csv")]

# Load DataFrames
dfs = [pd.read_csv(file_path) for file_path in file_paths]

# Output directories
output_dirs = {
    "cypher_dev": "LLM_results_processed_cypher_dev",
    "cypher_sample_test": "LLM_results_processed_cypher_sample_test",
    "cypher_sample_dev": "LLM_results_processed_cypher_sample_dev",
    "cypher_test": "LLM_results_processed_cypher_test",
    "sparql1_dev": "LLM_results_processed_sparql1_dev",
    "sparql2_dev": "LLM_results_processed_sparql2_dev",
    "sparql1_sample_dev": "LLM_results_processed_sparql1_sample_dev",
    "sparql2_sample_dev": "LLM_results_processed_sparql2_sample_dev",
    "sparql1_test": "LLM_results_processed_sparql1_test",
    "sparql2_test": "LLM_results_processed_sparql2_test",
    "sparql1_sample_test": "LLM_results_processed_sparql1_sample_test",
    "sparql2_sample_test": "LLM_results_processed_sparql2_sample_test",
    "sql_dev": "LLM_results_processed_sql_dev",
    "sql_test": "LLM_results_processed_sql_test",
    "sql_sample_dev": "LLM_results_processed_sql_sample_dev",
    "sql_sample_test": "LLM_results_processed_sql_sample_test",
    "mql_dev": "LLM_results_processed_mql_dev",
    "mql_test": "LLM_results_processed_mql_test",
    "mql_sample_dev": "LLM_results_processed_mql_sample_dev",
    "mql_sample_test": "LLM_results_processed_mql_sample_test"
}

# Ensure the output directories exist
for output_dir in output_dirs.values():
    os.makedirs(output_dir, exist_ok=True)

for i, df in enumerate(dfs):
    if "sample_dev" in file_paths[i]:
        comparison_df = sample_dev
    elif "sample_test" in file_paths[i]:
        comparison_df = sample_test
    elif "dev" in file_paths[i]:
        comparison_df = dev
    elif "test" in file_paths[i]:
        comparison_df = test
    else:
        continue

    output_dir = None
    if "sample_dev" in file_paths[i]:
        if "cypher" in file_paths[i]:
            output_dir = output_dirs["cypher_sample_dev"]
        elif "sparql1" in file_paths[i]:
            output_dir = output_dirs["sparql1_sample_dev"]
        elif "sparql2" in file_paths[i]:
            output_dir = output_dirs["sparql2_sample_dev"]
        elif "sql" in file_paths[i]:
            output_dir = output_dirs["sql_sample_dev"]
        elif "mql" in file_paths[i]:
            output_dir = output_dirs["mql_sample_dev"]
    elif "sample_test" in file_paths[i]:
        if "cypher" in file_paths[i]:
            output_dir = output_dirs["cypher_sample_test"]
        elif "sparql1" in file_paths[i]:
            output_dir = output_dirs["sparql1_sample_test"]
        elif "sparql2" in file_paths[i]:
            output_dir = output_dirs["sparql2_sample_test"]
        elif "sql" in file_paths[i]:
            output_dir = output_dirs["sql_sample_test"]
        elif "mql" in file_paths[i]:
            output_dir = output_dirs["mql_sample_test"]
    elif "dev" in file_paths[i]:
        if "cypher" in file_paths[i]:
            output_dir = output_dirs["cypher_dev"]
        elif "sparql1" in file_paths[i]:
            output_dir = output_dirs["sparql1_dev"]
        elif "sparql2" in file_paths[i]:
            output_dir = output_dirs["sparql2_dev"]
        elif "sql" in file_paths[i]:
            output_dir = output_dirs["sql_dev"]
        elif "mql" in file_paths[i]:
            output_dir = output_dirs["mql_dev"]
    elif "test" in file_paths[i]:
        if "cypher" in file_paths[i]:
            output_dir = output_dirs["cypher_test"]
        elif "sparql1" in file_paths[i]:
            output_dir = output_dirs["sparql1_test"]
        elif "sparql2" in file_paths[i]:
            output_dir = output_dirs["sparql2_test"]
        elif "sql" in file_paths[i]:
            output_dir = output_dirs["sql_test"]
        elif "mql" in file_paths[i]:
            output_dir = output_dirs["mql_test"]

    output_file = os.path.join(output_dir, os.path.basename(file_paths[i]))

    if os.path.exists(output_file):
        print(f"File {output_file} already exists.")
        df_existing = pd.read_csv(output_file)
        df.update(df_existing)
        processed_indices = df_existing[df_existing[df_existing.columns[-2]].notna()].index  # Assuming last but one column is *_results
        if len(processed_indices) > 0:
            start_index = processed_indices[-1] + 1
        else:
            start_index = 0

        if start_index >= len(comparison_df):
            print(f"File {output_file} already fully processed. Skipping.")
            continue
    else:
        start_index = 0

    if "cypher" in file_paths[i]:
        df.rename(columns={'answers': 'cypher_llm'}, inplace=True)
        df['cypher_llm_processed'] = df['cypher_llm'].apply(extract_cypher_query)
        df_processed = process_dataframe_cypher_llm(df, neo4j_uri, neo4j_user, neo4j_password, output_file, start_index)
    elif "sparql1" in file_paths[i]:
        df.rename(columns={'answers': 'sparql_llm'}, inplace=True)
        df['sparql_llm_processed'] = df['sparql_llm'].apply(extract_sparql_query)
        df_processed = process_dataframe_sparql_llm(df, graphdb_url, graphdb_user, graphdb_password, output_file, start_index)
    elif "sparql2" in file_paths[i]:
        df.rename(columns={'answers': 'sparql_llm'}, inplace=True)
        df['sparql_llm_processed'] = df['sparql_llm'].apply(extract_sparql_query)
        df_processed = process_dataframe_sparql_llm(df, graphdb_url, graphdb_user, graphdb_password, output_file, start_index)
    elif "sql" in file_paths[i]:
        df.rename(columns={'answers': 'sql_llm'}, inplace=True)
        df['sql_llm_processed'] = df['sql_llm'].apply(extract_sql_queries)
        #df_processed = process_dataframe_sql_llm(df, connection, output_file, start_index)
    elif "mql" in file_paths[i]:
        df.rename(columns={'answers': 'mql_llm'}, inplace=True)
        df['mql_llm_processed'] = df['mql_llm'].apply(extract_mongodb_query)
        #df_processed = process_dataframe_mql_llm(df, output_file, start_index)


