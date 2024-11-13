import os
import sys
import random
import argparse
import json
import requests
import re

import pandas as pd
import numpy as np
import google.generativeai as genai
import openai

# openai.api_key = os.environ["OPENAI_API_KEY"]
from openai import OpenAI
from groq import Groq

import time
import warnings

from prompts.bm25 import get_examples, get_examples_from_diverse_template

warnings.filterwarnings("ignore")


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

from prompts.schemas import *


def generate_statement_gpt(llm_model, formatted_prompt, retries=10):
    client = OpenAI(
        organization="org-0ETBijh97KRCc66SwxdqZYas",
        project="proj_PkZ1sRwgxenG2CNRjBHMRYPg",
    )
    for attempt in range(retries):
        try:
            start_time = time.time()
            completion = client.chat.completions.create(
                model=llm_model,
                temperature=0.0,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": formatted_prompt},
                ],
            )
            response = completion.choices[0].message.content
            end_time = time.time()
            elapsed_time = end_time - start_time
            return response.strip(), elapsed_time
        except Exception as e:
            print(f"Error occurred on attempt {attempt + 1}: {e}")
            if attempt == retries - 1:
                return "Could not answer the Question", None
            time.sleep(2)


def generate_statement_groq(llm_model, formatted_prompt, retries=20):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    for attempt in range(retries):
        try:
            start_time = time.time()
            completion = client.chat.completions.create(
                model=llm_model,
                temperature=0.0,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": formatted_prompt},
                ],
            )
            response = completion.choices[0].message.content
            end_time = time.time()
            elapsed_time = end_time - start_time
            return response.strip(), elapsed_time
        except Exception as e:
            print(f"Error occurred on attempt {attempt + 1}: {e}")
            if attempt == retries - 1:
                # Exit the program
                print("GIVING UP EXITING THE SCRIPT")
                sys.exit()
            # Extract the time to wait from the error message
            wait_time_match = re.search(
                r"Please try again in (\d+)m(\d+\.\d+)s", str(e)
            )
            if wait_time_match:
                minutes = int(wait_time_match.group(1))
                seconds = float(wait_time_match.group(2))
                wait_time = (minutes * 60 + seconds) + random.uniform(2, 4)
                print(f"Waiting for {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            else:
                # If the wait time is not found, use the original random sleep
                time.sleep(attempt * random.uniform(2, 4))

            time.sleep(attempt * random.uniform(2, 4))
        # random sleep to avoid rate limiting
        time.sleep(random.uniform(1, 2))


def generate_statement_gemini(formatted_prompt, retries=100):
    model = genai.GenerativeModel("gemini-pro")
    safety_settings = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]
    for attempt in range(retries):
        try:
            start_time = time.time()
            response = model.generate_content(
                formatted_prompt, safety_settings=safety_settings
            )
            end_time = time.time()
            elapsed_time = end_time - start_time
            return response.text.strip(), elapsed_time
        except Exception as e:
            print(f"Error occurred on attempt {attempt + 1}: {e}")
            if attempt == retries - 1:
                # Exit the program
                print("GIVING UP EXITING THE SCRIPT")
                sys.exit()
                return "Could not answer the Question", None
            time.sleep(attempt * random.uniform(4, 8))
        # random sleep to avoid rate limiting
        time.sleep(random.uniform(1, 2))


def generate_statement_llama3_8b(formatted_prompt, retries=10):
    url = "http://dgx-a100.cloudlab.zhaw.ch:9175/generate"
    payload = {"inputs": formatted_prompt, "parameters": {"max_new_tokens": 200}}
    headers = {"Content-Type": "application/json"}

    for attempt in range(retries):
        try:
            start_time = time.time()
            response = requests.post(url, json=payload, headers=headers)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if response.status_code == 200:
                return response.json().get("generated_text", ""), elapsed_time
            else:
                print(
                    f"Attempt {attempt + 1} failed with status code {response.status_code}: {response.text}"
                )
        except Exception as e:
            print(f"Error occurred on attempt {attempt + 1}: {e}")

        if attempt < retries - 1:
            time.sleep(attempt * random.uniform(2, 4))
    # return "Could not answer the Question", None
    print("GIVING UP EXITING THE SCRIPT")
    sys.exit()


def generate_statement_llama3_70b_local(formatted_prompt, retries=10):
    url = "http://dgx-a100.cloudlab.zhaw.ch:9175/generate"
    payload = {
        "inputs": formatted_prompt,
        "parameters": {"max_new_tokens": 200},
    }
    headers = {"Content-Type": "application/json"}

    for attempt in range(retries):
        try:
            start_time = time.time()
            response = requests.post(url, json=payload, headers=headers)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if response.status_code == 200:
                return response.json().get("generated_text", ""), elapsed_time
            else:
                print(
                    f"Attempt {attempt + 1} failed with status code {response.status_code}: {response.text}"
                )
        except Exception as e:
            print(f"Error occurred on attempt {attempt + 1}: {e}")

        if attempt < retries - 1:
            time.sleep(attempt * random.uniform(2, 4))
    print("GIVING UP EXITING THE SCRIPT")
    sys.exit()


def run_experiments(
    llm_models,
    datasets,
    query_languages,
    cypher_prompttypes,
    sql_prompttypes,
    sparql_prompttypes,
    mql_prompttypes,
    exp_name="",
    bm_shots=5,
):
    train_file = "../../data/dataset/train_dev/train.csv"
    for llm_model in llm_models:
        print(f"Running experiments for {llm_model}...")
        for dataset in datasets:
            print(f"Running experiments for {dataset}...")
            file_name = dataset + ".csv"
            if dataset == "dev" or dataset == "sample_dev":
                df = pd.read_csv("../../data/dataset/train_dev/" + file_name)
            if dataset == "test" or dataset == "sample_test":
                df = pd.read_csv("../../data/dataset/test/" + file_name)

            for query_language in query_languages:
                print(f"Running experiments for {query_language}...")
                if query_language == "cypher":
                    prompttypes = cypher_prompttypes
                    schema = cypher_schema
                elif query_language == "sql":
                    prompttypes = sql_prompttypes
                    schema = sql_schema
                elif query_language == "sparql1":
                    prompttypes = sparql_prompttypes
                    schema = sparql1_schema
                elif query_language == "sparql2":
                    prompttypes = sparql_prompttypes
                    schema = sparql2_schema
                elif query_language == "mql":
                    prompttypes = mql_prompttypes
                    schema = mql_schema
                else:
                    print("Invalid query language")
                    sys.exit()
                output_dir = f"../../data/results/{query_language}/{exp_name}/{dataset}"
                print(f"Output directory: {output_dir}")
                os.makedirs(output_dir, exist_ok=True)
                for prompt_name, prompt_value in prompttypes.items():
                    csv_file = f"{output_dir}/{dataset}_{query_language}_{prompt_name}_{llm_model}.csv"
                    progress_file = f"{output_dir}/progress_{dataset}_{query_language}_{prompt_name}_{llm_model}.json"

                    # check if csv file exists, but progress file does not exist
                    if os.path.exists(csv_file) and not os.path.exists(progress_file):
                        print(
                            f"Danger! {csv_file} exists, but {progress_file} does not exist Delete csv file manually. Exiting..."
                        )
                        sys.exit()

                    if os.path.exists(progress_file):
                        with open(progress_file, "r") as f:
                            progress = json.load(f)
                            start_index = progress["last_processed_index"] + 1
                    else:
                        start_index = 0

                    count = start_index

                    for index, question in enumerate(
                        df["question"][start_index:], start=start_index
                    ):
                        examples = None
                        if "bm25_with_template" in prompt_name:
                            # we need to build the example queries for bm25
                            examples = get_examples_from_diverse_template(train_file, question, query_language, bm_shots)
                            if query_language == "mql":
                                formatted_prompt = prompt_value.replace(
                                    "{schema}", schema
                                ).replace("{question}", question).replace("{examples}", examples)
                            else:
                                formatted_prompt = prompt_value.format(
                                    schema=schema, question=question, examples=examples
                                )
                        elif "bm25" in prompt_name:
                            # we need to build the example queries for bm25
                            examples = get_examples(train_file, question, query_language, bm_shots)
                            if query_language == "mql":
                                formatted_prompt = prompt_value.replace(
                                    "{schema}", schema
                                ).replace("{question}", question).replace("{examples}", examples)
                            else:
                                formatted_prompt = prompt_value.format(
                                    schema=schema, question=question, examples=examples
                                )
                        else:
                            if query_language == "mql":
                                formatted_prompt = prompt_value.replace(
                                    "{schema}", schema
                                ).replace("{question}", question)
                            else:
                                formatted_prompt = prompt_value.format(
                                    schema=schema, question=question
                                )
                        if llm_model == "gemini":
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_gemini(formatted_prompt)
                        elif llm_model == "llama3-8b":
                            ## print("LLM model not deployed {llm_model}")
                            ## sys.exit()
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_llama3_8b(formatted_prompt)
                        elif llm_model == "gpt-3.5-turbo-0125":
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_gpt(llm_model, formatted_prompt)
                        elif llm_model == "gpt-3.5-turbo-0125-batch":
                            task = {
                                "custom_id": exp_name
                                + "_"
                                + llm_model
                                + "_"
                                + dataset
                                + "_"
                                + query_language
                                + "_"
                                + prompt_name
                                + "_"
                                + str(index),
                                "method": "POST",
                                "url": "/v1/chat/completions",
                                "body": {
                                    "model": "gpt-3.5-turbo-0125",
                                    "temperature": 0.0,
                                    "messages": [
                                        {
                                            "role": "system",
                                            "content": "You are a helpful assistant.",
                                        },
                                        {"role": "user", "content": formatted_prompt},
                                    ],
                                },
                            }
                            # Create the file path
                            file_path = f"{exp_name}_{llm_model}_{dataset}_{query_language}.jsonl"
                            if "bm25" in prompt_name:
                                file_path = f"{exp_name}_{llm_model}_{dataset}_{query_language}_bm25_{bm_shots}.jsonl"
                            # Convert the task object to a JSON string
                            task_json = json.dumps(task)

                            # Write the JSON string to the file
                            with open(file_path, "a") as file:
                                file.write(task_json + "\n")

                            statement = "Batch processing"
                            elapsed_time = 0
                        elif llm_model == "llama3-70b-8192":
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_groq(llm_model, formatted_prompt)
                        elif llm_model == "llama3-70b-8192-local":
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_llama3_70b_local(formatted_prompt)
                        elif llm_model == "mixtral-8x7b-32768":
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_groq(llm_model, formatted_prompt)
                        elif llm_model == "gemma-7b-it":
                            (
                                statement,
                                elapsed_time,
                            ) = generate_statement_groq(llm_model, formatted_prompt)
                        else:
                            print("Invalid LLM model {llm_model}")
                            sys.exit()

                        # Save the result to the CSV file after each question
                        result_df = pd.DataFrame(
                            {
                                "question": [question],
                                "answers": [statement],
                                "time_taken": [elapsed_time],
                            }
                        )
                        if start_index == 0 and index == 0:
                            result_df.to_csv(csv_file, index=False)
                        else:
                            result_df.to_csv(
                                csv_file, mode="a", header=False, index=False
                            )

                        count += 1
                        print(f"{prompt_name}_Finished Question Number {count}")

                        # Save progress after each question
                        progress = {"last_processed_index": index}
                        with open(progress_file, "w") as f:
                            json.dump(progress, f)
                    print(f"Finished {prompt_name} for {dataset} in {llm_model}")


def main(
    cypher_prompttypes,
    sql_prompttypes,
    sparql_prompttypes,
    mql_prompttypes,
    exp_name="",
):
    parser = argparse.ArgumentParser(
        description="Configure LLM models, datasets, and query language"
    )

    parser.add_argument(
        "--llm_models",
        nargs="+",
        default=["llama3-8b"],
        help="List of LLM models (default: ['llama3-8b'])",
    )
    parser.add_argument(
        "--datasets",
        nargs="+",
        default=["dev", "test"],
        help="List of datasets (default: ['dev', 'test'])",
    )
    parser.add_argument(
        "--query_languages",
        nargs="+",
        default=["cypher"],
        help="List of query languages (default: ['cypher'])",
    )
    parser.add_argument(
        "--bm25_shots",
        type=int,
        default=0,
        help="Number of BM25 shots (default: 1)",
    )

    args = parser.parse_args()

    llm_models = args.llm_models
    datasets = args.datasets
    query_languages = args.query_languages
    bm_shots = args.bm25_shots

    print("LLM Models:", llm_models)
    print("Datasets:", datasets)
    print("Query Languages:", query_languages)

    print("Running the experiments...")
    run_experiments(
        llm_models,
        datasets,
        query_languages,
        cypher_prompttypes,
        sql_prompttypes,
        sparql_prompttypes,
        mql_prompttypes,
        exp_name=exp_name,
        bm_shots=bm_shots,
    )
