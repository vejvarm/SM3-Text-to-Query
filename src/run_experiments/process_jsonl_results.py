import os
import sys
import json
import csv

def process_jsonl_file(file_path):
    with open(file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            custom_id = data['custom_id']
            response_content = data['response']['body']['choices'][0]['message']['content']
            
            print(custom_id)
            # Split the custom_id into parts
            parts = custom_id.split('_')
            exp_name = parts[0]
            llm_model = parts[1]
            dataset = parts[2]
            query_language = parts[3]
            prompt_name = '_'.join(parts[4:-1])  # Join the remaining parts except the last one
            index = parts[-1]
            
            # Construct the folder path
            # folder_path = f"{exp_name}_LLM_output_{query_language}_{dataset}"
            folder_path = f"../../data/results/{query_language}/{exp_name}/{dataset}"
            
            # Construct the CSV file path
            csv_file_name = f"{dataset}_{query_language}_{prompt_name}_{llm_model}.csv"
            csv_file_path = os.path.join(folder_path, csv_file_name)
            
            # Write the response content to the CSV file
            with open(csv_file_path, 'r+', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                csv_writer = csv.writer(csv_file)
                rows = list(csv_reader)
                
                # Update the row corresponding to the index
                row_index = int(index) + 1  # Add 1 to account for the header row
                if row_index < len(rows):
                    rows[row_index][1] = response_content
                else:
                    # If the row doesn't exist, raise an error and abandon the script
                    raise ValueError(f"Row {row_index} does not exist in the CSV file: {csv_file_path}")
                
                # Write the updated rows back to the CSV file
                csv_file.seek(0)
                csv_writer.writerows(rows)
                csv_file.truncate()

def process_jsonl_files(input_path):
    if os.path.isfile(input_path):
        # Process a single JSONL file
        process_jsonl_file(input_path)
    elif os.path.isdir(input_path):
        # Process multiple JSONL files in a folder
        jsonl_files = [file for file in os.listdir(input_path) if file.endswith(".jsonl")]
        for jsonl_file in jsonl_files:
            file_path = os.path.join(input_path, jsonl_file)
            process_jsonl_file(file_path)
    else:
        print(f"Invalid input path: {input_path}")

# Check if the input path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the input file or folder path as a command-line argument.")
    sys.exit(1)

input_path = sys.argv[1]

# Process the JSONL files
try:
    process_jsonl_files(input_path)
except ValueError as e:
    print(f"Error: {str(e)}")
    print("Abandoning the script.")
