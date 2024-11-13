import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import threading
import time
import os

class TimeoutException(Exception):
    pass

def execute_sparql_query_with_timeout(query, url, user, password, timeout=300):
    def sparql_query():
        try:
            nonlocal results, exec_time
            start_time = time.time()
            sparql = SPARQLWrapper(url)
            sparql.setCredentials(user, password)
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            exec_time = time.time() - start_time
        except Exception as e:
            nonlocal error
            error = e

    results = None
    exec_time = None
    error = None

    thread = threading.Thread(target=sparql_query)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        raise TimeoutException(f"Query exceeded the time limit of {timeout} seconds")

    if error:
        raise error

    return results, exec_time

def add_sparql_results_columns(df, columns, url, user, password, start_index=0, timeout=1500, output_file=None):
    for index in range(start_index, len(df)):
        for column in columns:
            query = str(df.at[index, column])
            print(f"Processing index {index} for column {column}, query: {query}")
            try:
                sparql_results, exec_time = execute_sparql_query_with_timeout(query, url, user, password, timeout)
                df.at[index, f'{column}_results'] = sparql_results
                df.at[index, f'{column}_query_time'] = exec_time
            except TimeoutException as e:
                print(f"Timeout occurred for index {index}: {e}")
                df.at[index, f'{column}_results'] = None
                df.at[index, f'{column}_query_time'] = None
            except Exception as e:
                print(f"Error occurred for index {index}: {e}")
                df.at[index, f'{column}_results'] = None
                df.at[index, f'{column}_query_time'] = None

        if output_file:
            df.to_csv(output_file, index=False)
            print(f"Saved progress to {output_file}")

    return df

def process_dataframe_sparql(df, url, user, password, output_file=None, start_index=0):
    # Add SPARQL results for 'sql' column
    df = add_sparql_results_columns(df, ['sparql'], url, user, password, start_index=start_index, output_file=output_file)
    return df

def process_dataframe_sparql_llm(df, url, user, password, output_file=None, start_index=0):
    # Add SPARQL results for both 'sparql_llm' and 'sparql_llm_processed' columns
    df = add_sparql_results_columns(df, ['sparql_llm_processed'], url, user, password, start_index=start_index, output_file=output_file)
    return df

if __name__ == "__main__":
    # Example how to use the functions

    # GraphDB Configurations
    url = "http://160.85.252.225:7200/repositories/Synthea3"
    user = "admin"
    password = "root"

    input_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/python/modules/LLM_output_sparql/QA_sparql_prompt_schema_fewshots_gemini.csv")
    # Process the Dataframe
    output_file = "C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/python/modules/LLM_output_sparql/QA_sparql_prompt_schema_fewshots_gemini_processed.csv"
    processed_df = process_dataframe_sparql_llm(input_df, url, user, password, output_file)

    print(processed_df)
    
    train_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/solutions/train.csv")
    # Process the Dataframe
    output_file = "C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/solutions/train_processed.csv"
    processed_df = process_dataframe_sparql_llm(train_df, url, user, password, output_file)
    
    print(processed_df)