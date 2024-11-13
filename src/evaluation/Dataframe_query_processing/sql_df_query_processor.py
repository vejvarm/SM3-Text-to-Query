import os
import pandas as pd
import re
import psycopg2
import time
from threading import Thread

dbname = "postgres"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

def extract_sql_queries(text):
    if isinstance(text, str):
        pattern = r'SELECT.*?;|SELECT.*?(?=\[Q\])'
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            matched_query = match.group(0).strip().replace('\n', ' ')
            return matched_query
        else:
            return text.strip()
    else:
        return ''

def thread_execute_sql_query(cursor, query, result):
    try:
        cursor.execute(query)
        result['records'] = cursor.fetchall()
        result['error'] = None
    except Exception as e:
        result['records'] = None
        result['error'] = e


def execute_sql_query(query, connection, timeout=120, retries=3):
    for attempt in range(retries):
        start_time = time.time()
        cursor = connection.cursor()
        result = {}
        thread = Thread(target=thread_execute_sql_query, args=(cursor, query, result))
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print(f"Timeout Error: Query execution exceeded {timeout} seconds on attempt {attempt + 1}")
            cursor.close()
            end_time = time.time()
            execution_time = end_time - start_time
            if attempt < retries - 1:
                print(f"Retrying query... (Attempt {attempt + 2})")
                continue
            else:
                return None, execution_time
        end_time = time.time()
        execution_time = end_time - start_time
        cursor.close()
        if result.get('error'):
            print(f"SQL Error: {result['error']} on attempt {attempt + 1}")
            connection.rollback()
            if attempt < retries - 1:
                print(f"Retrying query... (Attempt {attempt + 2})")
                continue
            else:
                return None, execution_time
        return result.get('records'), execution_time
    return None, execution_time

def add_sql_results_columns(df, columns, connection, start_index=0, output_file=None):
    for index in range(start_index, len(df)):
        for column in columns:
            query = str(df.at[index, column])
            print(f"Processing index {index} for column {column}, query: {query}")
            try:
                sql_results, exec_time = execute_sql_query(query, connection)
                df.at[index, f'{column}_results'] = sql_results
                df.at[index, f'{column}_query_time'] = exec_time
            except Exception as e:
                print(f"Error occurred for index {index} in column {column}: {e}")
                df.at[index, f'{column}_results'] = None
                df.at[index, f'{column}_query_time'] = None

        if output_file:
            df.to_csv(output_file, index=False)
            print(f"Saved progress to {output_file}")

    return df


def process_dataframe_sql(df, connection, output_file=None, start_index=0):
    # Add SPARQL results for 'sql' column
    df = add_sql_results_columns(df, ['sql'], connection, start_index=start_index, output_file=output_file)
    return df
def process_dataframe_sql_llm(df, connection, output_file=None, start_index=0):
    # Add SQL results for both 'sql_llm' and 'sql_llm_processed' columns
    df = add_sql_results_columns(df, ['sql_llm_processed'], connection, start_index=start_index, output_file=output_file)
    return df

if __name__ == "__main__":
    # Example how to use the functions

    #DB Postgres
    dbname = "postgres"
    user = "postgres"
    password = "postgres"
    host = "localhost"
    port = "5432"

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    input_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/python/modules/LLM_output_cypher/QA_cypher_prompt_schema_fewshots_llama3.csv")
    # Process the Dataframe
    processed_df = process_dataframe_sql_llm(input_df, conn)

    print(processed_df)

    train_df = pd.read_csv("C:/Users/Sithu/Documents/GitHub/SOMMED-QA/src/main/solutions/train.csv")
    # Process the Dataframe
    processed_df = process_dataframe_sql(train_df, conn)
    print(processed_df)