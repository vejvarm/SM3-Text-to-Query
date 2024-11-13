import csv
import os
import sys

csv.field_size_limit(sys.maxsize)


def remove_columns_from_csv(file_path, columns_to_remove):
    # Open the CSV file
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        # Check if the specified columns exist in the CSV file
        columns_to_delete = [col for col in columns_to_remove if col in fieldnames]

        # If no columns to delete, return without modifying the file
        if not columns_to_delete:
            print(f"No columns to delete in {file_path}. The file remains unchanged.")
            return

        # Create a new fieldnames list without the columns to delete
        updated_fieldnames = [col for col in fieldnames if col not in columns_to_delete]

        # Create a temporary file to write the updated CSV data
        temp_file_path = file_path + ".tmp"
        with open(temp_file_path, "w", newline="") as temp_file:
            writer = csv.DictWriter(temp_file, fieldnames=updated_fieldnames)
            writer.writeheader()

            # Write the rows to the temporary file, excluding the columns to delete
            for row in reader:
                updated_row = {col: row[col] for col in updated_fieldnames}
                writer.writerow(updated_row)

    # Replace the original file with the updated file
    os.replace(temp_file_path, file_path)
    print(f"Columns {columns_to_delete} deleted from {file_path}.")


def process_csv_files(path, columns_to_remove):
    if os.path.isfile(path):
        if path.lower().endswith(".csv"):
            remove_columns_from_csv(path, columns_to_remove)
        else:
            print(f"{path} is not a CSV file. Skipping.")
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if file_path.lower().endswith(".csv"):
                remove_columns_from_csv(file_path, columns_to_remove)
    else:
        print(f"{path} is not a valid file or directory.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_or_folder_path>")
        sys.exit(1)

    path = sys.argv[1]
    columns_to_remove = [
        "cypher_results",
        "cypher_query_time",
        "sparql_results",
        "sparql_query_time",
        "sql_results",
        "sql_query_time",
        "mql_results",
        "mql_query_time",
    ]

    process_csv_files(path, columns_to_remove)
