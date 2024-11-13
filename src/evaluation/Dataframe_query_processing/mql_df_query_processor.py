import pandas as pd
import re
import time
import os
import subprocess
from pymongo import MongoClient

def execute_mongo_query(query):
    start_time = time.time()
    records = "[]"
    try:
        process = subprocess.Popen(["mongosh", "--quiet", "healthcare"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=query)
        
        # Check if there was an error
        if stderr:
            records = f"Error: {stderr.strip()}"
        else:
            # Check if stdout contains a MongoDB error message
            error_pattern = re.compile(r'Error: .*')
            error_match = error_pattern.search(stdout.strip())
            if error_match:
                error_message = error_match.group()
                records = error_message
            else:
                # Extract the results from the output
                results_pattern = re.compile(r'\[([\s\S]*?)\]')
                results_match = results_pattern.search(stdout.strip())
                if results_match:
                    records = results_match.group(1)
                    records = re.sub(r'\s+', ' ', records).strip()
    except Exception as e:
        records = f"Error: {str(e)}"
    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        return records, execution_time

def add_mql_results_columns(df, columns, output_file=None):
    start_index = 0

    if output_file and os.path.exists(output_file):
        df_existing = pd.read_csv(output_file)
        df.update(df_existing)
        start_index = df_existing[df_existing[f'{columns[0]}_results'].notna()].shape[0]
        if start_index >= len(df):
            print(f"File {output_file} already fully processed. Skipping.")
            return df_existing

    for index in range(start_index, len(df)):
        for column in columns:
            query = str(df.at[index, column])
            print(f"Processing index {index} for column {column}, query: {query}")
            if query.lower().startswith("no"):
                mql_results, exec_time = "No answer possible based on given input", 0
                df.at[index, f'{column}_results'] = mql_results
                df.at[index, f'{column}_query_time'] = exec_time
            try:
                mql_results, exec_time = execute_mongo_query(query)
                #print(f"Results for index {index} in column {column}: {sql_results}, Time: {exec_time}")
                df.at[index, f'{column}_results'] = mql_results
                df.at[index, f'{column}_query_time'] = exec_time
            except Exception as e:
                print(f"Error occurred for index {index} in column {column}: {e}")
                df.at[index, f'{column}_results'] = None
                df.at[index, f'{column}_query_time'] = None

        if output_file:
            df.to_csv(output_file, index=False)
            print(f"Saved progress to {output_file}")
    return df

## Sithu version Bekommt indexnummer vom mainfile. 
def add_mql_results_columns2(df, columns, start_index=0, output_file=None):
    # client = MongoClient("mongodb://localhost:27017/")
    for index in range(start_index, len(df)):
        for column in columns:
            query = str(df.at[index, column])
            print(f"Processing index {index} for column {column}, query: {query}")
            if query.lower().startswith("no"):
                mql_results, exec_time = "No answer possible based on given input", 0
                df.at[index, f'{column}_results'] = mql_results
                df.at[index, f'{column}_query_time'] = exec_time
            else:
                try:
                    mql_results, exec_time = execute_mongo_query(query)
                    df.at[index, f'{column}_results'] = mql_results
                    df.at[index, f'{column}_query_time'] = exec_time
                except Exception as e:
                    print(f"Error occurred for index {index} in column {column}: {e}")
                    df.at[index, f'{column}_results'] = None
                    df.at[index, f'{column}_query_time'] = None

        if output_file:
            df.to_csv(output_file, index=False)
            print(f"Saved progress to {output_file}")

    return df


def process_dataframe_mql(df, output_file=None, append_file=None):
    # Add SPARQL results for 'sql' column
    df = add_mql_results_columns2(df, ['mql'])
    if append_file:
        # check the file exists
        if os.path.exists(append_file):
            df_existing = pd.read_csv(append_file)
            # concat []"mql", "mql_results", "mql_query_time"] to the df_existing
            df_existing = pd.concat([df_existing, df[["mql", "mql_results", "mql_query_time"]]], axis=1)
            # rearrange the columns to the order question,sparql,sql,cypher,mql,question_type,class,cypher_results,cypher_query_time,sparql_results,sparql_query_time,sql_results,sql_query_time,mql_results,mql_query_time
            df_existing = df_existing[["question","sparql","sql","cypher","mql","question_type","class","cypher_results","cypher_query_time","sparql_results","sparql_query_time","sql_results","sql_query_time","mql_results","mql_query_time"]]
            # append the columns [] to the df_existing
            df = df_existing
            print(f"Appended to {append_file}")
            df.to_csv(append_file, index=False)
        else:
            raise Exception(f"File {append_file} does not exist.")
    elif output_file:
        if os.path.exists(output_file):
            raise Exception(f"File {output_file} already exists. Please provide a new file name.")
        else:
            print(f"File {output_file} does not exist. Creating new file.")
            df.to_csv(output_file, index=False)
    return df

def process_dataframe_mql_llm(df, output_file=None, start_index=0):
    #print("Processing 'mql_llm' and 'mql_llm_processed' columns")
    df = add_mql_results_columns2(df, ['mql_llm_processed'], start_index=start_index, output_file=output_file)
    return df


if __name__ == "__main__":
    # Example how to use the functions

    # input_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/python/modules/LLM_output_cypher/QA_cypher_prompt_schema_fewshots_llama3.csv")
    input_df = pd.read_csv("../raw_data/corrected_test.csv")
    # Process the Dataframe
    processed_df = process_dataframe_mql(input_df, output_file=None, append_file="../processed_data/processed_test.csv")

    
    """
    train_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/solutions/train.csv")
    # Process the Dataframe
    processed_df = process_dataframe_sql(train_df, conn)
    print(processed_df)
    """