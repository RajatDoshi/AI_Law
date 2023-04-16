from my_data import *
import json

# 
with open("data.jsonl", "w") as f:
    for d in training_examples:
        json.dump(d, f)
        f.write('\n')