import sys
from openai import OpenAI
client = OpenAI()

# get batch name 
if len(sys.argv) < 2:
    print("Please provide the batch ID as a command-line argument.")
    sys.exit(1)
else:
    client.batches.retrieve(sys.argv[1])