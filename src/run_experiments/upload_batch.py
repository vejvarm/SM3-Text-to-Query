import os
import sys
from openai import OpenAI
from pathlib import Path

def process_jsonl_file(client, file_path):
    try:
        batch_input_file = client.files.create(
            file=open(file_path, "rb"),
            purpose="batch"
        )
        print(f"Batch file '{file_path}' uploaded successfully.")
        batch_input_file_id = batch_input_file.id
        print("ID:", batch_input_file_id)
        resp = client.batches.create(
            input_file_id=batch_input_file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": "nightly eval job"
            }
        )
        print(resp)
    except FileNotFoundError:
        print(f"Batch file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while uploading the batch file: {str(e)}")

def process_jsonl_files(client, input_path):
    if os.path.isfile(input_path):
        # Process a single JSONL file
        process_jsonl_file(client, input_path)
    elif os.path.isdir(input_path):
        # Process multiple JSONL files in a folder
        jsonl_files = [file for file in os.listdir(input_path) if file.endswith(".jsonl")]
        for jsonl_file in jsonl_files:
            file_path = os.path.join(input_path, jsonl_file)
            process_jsonl_file(client, file_path)
    else:
        print(f"Invalid input path: {input_path}")

# Check if the input path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the input file or folder path as a command-line argument.")
    sys.exit(1)

else:
    cwd = Path.cwd()
    if sys.argv[1].startswith("/"):
        input_path = sys.argv[1]
    else:
        input_path = str(cwd / sys.argv[1]) # Convert to absolute path

assert Path(input_path).exists(), f"Input path '{input_path}' does not exist."
assert Path(input_path).is_dir(), f"Input path '{input_path}' is not a directory."

client = OpenAI()
process_jsonl_files(client, input_path)