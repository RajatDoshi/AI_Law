from my_data import *
import json

# Convert the data to the format expected by the library
with open("training_data.jsonl", "w") as f:
    for d in training_examples:
        json.dump(d, f)
        f.write('\n')

# Convert the data to the format expected by the library


def convert_data(data):
    with open("training_data.jsonl", "w") as f:
        for d in data:
            json.dump(d, f)
            f.write('\n')

# convert_data(training_examples)


# Convert json to jsonl
def convert_json_to_jsonl(file):
    with open(file, 'r') as f:
        data = json.load(f)
    with open(file + ".jsonl", "w") as f:
        for d in data:
            json.dump(d, f)
            f.write('\n')


# convert jsonl to json
def convert_jsonl_to_json(file):
    with open(file, 'r') as f:
        data = f.readlines()
    data = [json.loads(d) for d in data]
    with open(file + ".json", "w") as f:
        json.dump(data, f)
