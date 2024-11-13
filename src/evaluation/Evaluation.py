import pandas as pd
import glob
import os
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# Function to dynamically find all input directories matching the pattern
def find_input_dirs(base_pattern="LLM_results_processed_"):
    input_dirs = {}
    for entry in os.listdir('.'):
        if os.path.isdir(entry):
            if base_pattern in entry:
                if entry.startswith("LLM_results_processed_"):
                    key = entry[len("LLM_results_processed_"):]
                else:
                    key = entry  # Keep the prefix for keys starting with EXP2_
                input_dirs[key] = os.path.join('.', entry)
    return input_dirs

input_dirs = find_input_dirs()
# Output directories for cleaned data
cleaned_output_dirs = {key: os.path.join("cleaned_LLM_results", key) for key in input_dirs.keys()}
# Function to update reference dataframes based on question_type
def update_unanswerable_references(df):
    unanswerable_types = ["unanswerable_medical", "unanswerable_non_medical"]
    for query_lang in ["cypher", "sparql", "sql", "mql"]:
        df.loc[df["question_type"].isin(unanswerable_types), f"{query_lang}_results"] = "No answer possible based on given input"

# Load and update the reference dataframes
test_df = pd.read_csv("test.csv")
dev_df = pd.read_csv("dev.csv")
sample_dev_df = pd.read_csv("sample_dev.csv")
sample_test_df = pd.read_csv("sample_test.csv")

update_unanswerable_references(test_df)
update_unanswerable_references(dev_df)
update_unanswerable_references(sample_dev_df)
update_unanswerable_references(sample_test_df)

# TODO FIXME this function needs to do something more smart than just comparing for equal srtrings!
def calculate_execution_accuracy(df, column1, column2, result_col_name):
    total_queries = len(df)
    comparison = df[column1] == df[column2]
    correct_count = comparison.sum()
    execution_accuracy = (correct_count / total_queries) * 100
    df[result_col_name] = comparison.astype(int)
    return execution_accuracy

def calculate_accuracy(df, column1, column2, result_col_name):
    accuracies = []
    for index, row in df.iterrows():
        query1 = str(row[column1])
        query2 = str(row[column2])
        similarity_score = fuzz.token_sort_ratio(query1, query2)
        accuracy = 1 if similarity_score >= 100 else 0
        accuracies.append(accuracy)
    overall_accuracy = (sum(accuracies) / len(df)) * 100
    df[result_col_name] = accuracies
    return overall_accuracy

def calculate_cosine_similarity(df, column1, column2, result_col_name):
    df[column1].fillna('', inplace=True)
    df[column2].fillna('', inplace=True)
    vectorizer = TfidfVectorizer()
    combined_text = df[column1] + " " + df[column2]
    vectorizer.fit(combined_text)
    vector_query1 = vectorizer.transform(df[column1]).toarray()
    vector_query2 = vectorizer.transform(df[column2]).toarray()
    cosine_similarities = cosine_similarity(vector_query1, vector_query2)
    df[result_col_name] = cosine_similarities.diagonal()
    overall_cosine_similarity = cosine_similarities.diagonal().mean() * 100
    return overall_cosine_similarity

def calculate_ves(df, or_query_time, or_results, results, query_time, result_col_name):
    if df[or_query_time].isnull().any() or df[query_time].isnull().any():
        df[or_query_time].fillna(0, inplace=True)
        df[query_time].fillna(0, inplace=True)

    if not np.isfinite(df[or_query_time]).all() or not np.isfinite(df[query_time]).all():
        df[or_query_time].replace([np.inf, -np.inf], 0, inplace=True)
        df[query_time].replace([np.inf, -np.inf], 0, inplace=True)

    N = len(df)
    VES_sum = 0

    for i in range(N):
        R_Y = np.sqrt(df[or_query_time].iloc[i] / df[query_time].iloc[i]) if df[or_query_time].iloc[i] != 0 and df[query_time].iloc[i] != 0 else 0
        indicator = 1 if df[or_results].iloc[i] == df[results].iloc[i] else 0
        VES_sum += indicator * R_Y

    VES = VES_sum / N if N > 0 else np.nan
    df[result_col_name] = VES
    return VES * 100

def extract_info_from_filename(filename):
    base = os.path.basename(filename)
    folder = os.path.basename(os.path.dirname(filename))
    folder_parts = folder.split('_')
    
    experiment_number = 1  # Default to 1 if no EXP prefix is found
    if any(part.startswith('EXP') and part[3:].isdigit() for part in folder_parts):
        experiment_part = next(part for part in folder_parts if part.startswith('EXP') and part[3:].isdigit())
        experiment_number = int(experiment_part[3:])  # Extract the number after EXP
        folder_parts.remove(experiment_part)  # Remove the EXP part for correct dataset extraction

    # Determine the dataset
    if len(folder_parts) >= 2 and folder_parts[-2] == 'sample':
        dataset = '_'.join(folder_parts[-2:])
    else:
        dataset = folder_parts[-1]
    
    parts = base.split('_')
    prompt = '_'.join(parts[2:-1])  # Extract the prompt

    # Map the prompt names according to the specified changes
    prompt_mapping = {
        '0schema_fewshots': '5-shots',
        '0schema_oneshot': '1-shot',
        'schema_fewshots': 'Schema & 5-shots',
        'schema_0shot': 'Schema',
        'schema_oneshot': 'Schema & 1-shot'
    }
    
    for key, value in prompt_mapping.items():
        if key in prompt:
            prompt = value
            break

    # Extract the LLM using pattern search
    llm_patterns = {
        'gemini': 'gemini',
        'llama3-8b': 'llama3-8b',
        'llama3-8b': 'llama3_8b',
        'llama3-70b-8192': 'llama3-70b-8192',
        'gpt-3.5-turbo-0125': 'gpt-3.5-turbo-0125'
    }

    llm = None
    for llm_name, pattern in llm_patterns.items():
        if pattern in base:
            llm = llm_name
            break
    
    if llm is None:
        llm = base.split('_')[-1].split('.')[0]  # Fallback to the last part if no pattern matched

    return dataset, llm, prompt, experiment_number

def transform_dataframe(df, filename):
    dataset, llm, prompt, experiment_number = extract_info_from_filename(filename)
    df['Dataset'] = dataset
    df['LLM'] = llm
    df['Prompt'] = prompt
    df['Experiment_number'] = experiment_number
    
    if 'sql_llm_processed_results' in df.columns:
        df['Query Language'] = 'sql'
        rename_columns = {
            'sql': 'original_query',
            'sql_llm_processed': 'llm_processed_query',
            'sql_results': 'original_result',
            'sql_llm_processed_results': 'llm_processed_result',
            'sql_query_time': 'original_time',
            'sql_llm_processed_query_time': 'llm_processed_query_time',
            'time_taken': 'LLM_generation_time'
        }
    elif 'cypher_llm_processed_results' in df.columns:
        df['Query Language'] = 'cypher'
        rename_columns = {
            'cypher': 'original_query',
            'cypher_llm_processed': 'llm_processed_query',
            'cypher_results': 'original_result',
            'cypher_llm_processed_results': 'llm_processed_result',
            'cypher_query_time': 'original_time',
            'cypher_llm_processed_query_time': 'llm_processed_query_time',
            'time_taken': 'LLM_generation_time'
        }
    elif 'sparql_llm_processed_results' in df.columns:
        if 'sparql1' in filename:
            df['Query Language'] = 'sparql1'
        elif 'sparql2' in filename:
            df['Query Language'] = 'sparql2'
        else:
            print("not SPARQL")
        rename_columns = {
            'sparql': 'original_query',
            'sparql_llm_processed': 'llm_processed_query',
            'sparql_results': 'original_result',
            'sparql_llm_processed_results': 'llm_processed_result',
            'sparql_query_time': 'original_time',
            'sparql_llm_processed_query_time': 'llm_processed_query_time',
            'time_taken': 'LLM_generation_time'
        }
    elif 'mql_llm_processed_results' in df.columns:
        df['Query Language'] = 'mql'
        rename_columns = {
            'mql': 'original_query',
            'mql_llm_processed': 'llm_processed_query',
            'mql_results': 'original_result',
            'mql_llm_processed_results': 'llm_processed_result',
            'mql_query_time': 'original_time',
            'mql_llm_processed_query_time': 'llm_processed_query_time',
            'time_taken': 'LLM_generation_time'
        }
    else:
        rename_columns = {}

    df.rename(columns=rename_columns, inplace=True)
    
    columns_to_keep = [
        'Dataset', 'LLM', 'Query Language', 'Prompt', 'original_query', 'llm_processed_query',
        'original_result', 'llm_processed_result', 'original_time', 'llm_processed_query_time', 'LLM_generation_time',
        'execution_accuracy_processed', 'query_accuracy_processed', 'cosine_similarity_processed',
        'ves_processed', 'Experiment_number'
    ]
    
    return df[[col for col in columns_to_keep if col in df.columns]]

def update_llm_queries(df):
    pattern = re.compile(r".*No answer possible based on given input.*", re.IGNORECASE)
    for query_lang in ["sql", "cypher", "sparql", "mql"]:
        llm_col = f"{query_lang}_llm"
        processed_col = f"{query_lang}_llm_processed"
        results_col = f"{query_lang}_llm_processed_results"
        if llm_col in df.columns:
            no_answer_mask = df[llm_col].apply(lambda x: bool(pattern.match(str(x))))
            df.loc[no_answer_mask, processed_col] = "No answer possible based on given input"
            df.loc[no_answer_mask, results_col] = "No answer possible based on given input"

def process_dataframes(input_dirs, cleaned_output_dirs, test_df, dev_df, sample_dev_df, sample_test_df, output_excel_file):
    results = []
    cleaned_merged_df = pd.DataFrame()

    for key in input_dirs.keys():
        input_dir = input_dirs[key]
        files = glob.glob(os.path.join(input_dir, "*.csv"))
        
        for idx, file in enumerate(files):
            df = pd.read_csv(file)
            print(f"Processing DataFrame {idx + 1}/{len(files)}: {file}")

            # Identify the correct reference DataFrame based on the file name
            filename = os.path.basename(file)
            if 'sample' in filename and 'test' in filename:
                reference_df = sample_test_df
                ref_type = 'sample_test'
            elif 'sample' in filename and 'dev' in filename:
                reference_df = sample_dev_df
                ref_type = 'sample_dev'
            elif 'test' in filename:
                reference_df = test_df
                ref_type = 'test'
            else:
                reference_df = dev_df
                ref_type = 'dev'
            
            print(f"Using {ref_type} reference DataFrame for file: {file}")

            # Determine which columns to add based on presence in the DataFrame
            if 'sql_llm_processed_results' in df.columns:
                columns_to_add = ['sql', 'sql_results', 'sql_query_time']
            elif 'cypher_llm_processed_results' in df.columns:
                columns_to_add = ['cypher', 'cypher_results', 'cypher_query_time']
            elif 'sparql_llm_processed_results' in df.columns:
                columns_to_add = ['sparql', 'sparql_results', 'sparql_query_time']
            elif 'mql_llm_processed_results' in df.columns:
                columns_to_add = ['mql', 'mql_results', 'mql_query_time']
            else:
                print(f"No relevant columns found in {file}. Skipping.")
                continue

            # Add appropriate columns from the reference dataframe
            for col in columns_to_add:
                df[col] = reference_df[col]
            
            metrics = {'filename': os.path.basename(file), 'folder': os.path.basename(input_dir)} #Excel Folder and Filename
            
            # Update the DataFrame for LLM queries
            update_llm_queries(df)

            # Execute calculations and analyses for SQL results if SQL columns are present
            if 'sql_results' in df.columns and 'sql_llm_processed_results' in df.columns:
                metrics['sql_execution_accuracy_processed'] = calculate_execution_accuracy(df, 'sql_results', 'sql_llm_processed_results', 'execution_accuracy_processed')
                metrics['sql_query_accuracy_processed'] = calculate_accuracy(df, 'sql', 'sql_llm_processed', 'query_accuracy_processed')
                metrics['sql_cosine_similarity_processed'] = calculate_cosine_similarity(df, 'sql', 'sql_llm_processed', 'cosine_similarity_processed')
                metrics['sql_ves_processed'] = calculate_ves(df, 'sql_query_time', 'sql_results', 'sql_llm_processed_results', 'sql_llm_processed_query_time', 'ves_processed')
            
            # Execute calculations and analyses for Cypher results if Cypher columns are present
            if 'cypher_results' in df.columns and 'cypher_llm_processed_results' in df.columns:
                metrics['cypher_execution_accuracy_processed'] = calculate_execution_accuracy(df, 'cypher_results', 'cypher_llm_processed_results', 'execution_accuracy_processed')
                metrics['cypher_query_accuracy_processed'] = calculate_accuracy(df, 'cypher', 'cypher_llm_processed', 'query_accuracy_processed')
                metrics['cypher_cosine_similarity_processed'] = calculate_cosine_similarity(df, 'cypher', 'cypher_llm_processed', 'cosine_similarity_processed')
                metrics['cypher_ves_processed'] = calculate_ves(df, 'cypher_query_time', 'cypher_results', 'cypher_llm_processed_results', 'cypher_llm_processed_query_time', 'ves_processed')
            
            # Execute calculations and analyses for SPARQL results if SPARQL columns are present
            if 'sparql_results' in df.columns and 'sparql_llm_processed_results' in df.columns:
                metrics['sparql_execution_accuracy_processed'] = calculate_execution_accuracy(df, 'sparql_results', 'sparql_llm_processed_results', 'execution_accuracy_processed')
                metrics['sparql_query_accuracy_processed'] = calculate_accuracy(df, 'sparql', 'sparql_llm_processed', 'query_accuracy_processed')
                metrics['sparql_cosine_similarity_processed'] = calculate_cosine_similarity(df, 'sparql', 'sparql_llm_processed', 'cosine_similarity_processed')
                metrics['sparql_ves_processed'] = calculate_ves(df, 'sparql_query_time', 'sparql_results', 'sparql_llm_processed_results', 'sparql_llm_processed_query_time', 'ves_processed')

            # Execute calculations and analyses for MQL results if MQL columns are present
            if 'mql_results' in df.columns and 'mql_llm_processed_results' in df.columns:
                metrics['mql_execution_accuracy_processed'] = calculate_execution_accuracy(df, 'mql_results', 'mql_llm_processed_results', 'execution_accuracy_processed')
                metrics['mql_query_accuracy_processed'] = calculate_accuracy(df, 'mql', 'mql_llm_processed', 'query_accuracy_processed')
                metrics['mql_cosine_similarity_processed'] = calculate_cosine_similarity(df, 'mql', 'mql_llm_processed', 'cosine_similarity_processed')
                metrics['mql_ves_processed'] = calculate_ves(df, 'mql_query_time', 'mql_results', 'mql_llm_processed_results', 'mql_llm_processed_query_time', 'ves_processed')

            results.append(metrics)

            # Transform the dataframe
            transformed_df = transform_dataframe(df, file)

            # Append the transformed DataFrame to the cleaned_merged_df
            cleaned_merged_df = pd.concat([cleaned_merged_df, transformed_df], ignore_index=True)

    # Save all metrics to an Excel file
    all_results_df = pd.DataFrame(results)
    all_results_df.to_excel(output_excel_file, index=False)
    print(f"All DataFrames processed successfully. Results saved to {output_excel_file}")

    # Save the cleaned merged DataFrame to a CSV file
    cleaned_merged_df.to_csv("cleaned_merged_df.csv", index=False)
    print("Cleaned merged DataFrame saved to cleaned_merged_df.csv")

process_dataframes(input_dirs, cleaned_output_dirs, test_df, dev_df, sample_dev_df, sample_test_df, "evaluation_results.xlsx")
