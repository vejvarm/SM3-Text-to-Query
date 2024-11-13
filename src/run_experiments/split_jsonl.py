import argparse
import json

def split_jsonl_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    mid = num_lines // 2

    output_file1 = filename.replace('.jsonl', '_part1.jsonl')
    output_file2 = filename.replace('.jsonl', '_part2.jsonl')

    with open(output_file1, 'w') as file1, open(output_file2, 'w') as file2:
        for i, line in enumerate(lines):
            if i < mid:
                file1.write(line)
            else:
                file2.write(line)

    print(f"Split {filename} into {output_file1} and {output_file2}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split a JSONL file into two files.')
    parser.add_argument('filename', type=str, help='The JSONL file to be split')
    args = parser.parse_args()

    split_jsonl_file(args.filename)
