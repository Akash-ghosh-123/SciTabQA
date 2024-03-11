import json
import pandas as pd
import pickle

with open('COLING_dataset_final/question_answer_pairs.pkl', 'rb') as f1:
    qa = pickle.load(f1)
with open('COLING_dataset_final/train_tables.pkl', 'rb') as f2:
    trn = pickle.load(f2)
with open('COLING_dataset_final/dev_tables.pkl', 'rb') as f3:
    dev = pickle.load(f3)

print(len(qa))
print(len(trn))
print(len(dev))

print(qa[1])
print(trn[1])
print(dev[1])

print(qa[49])
print(trn[49])
print(dev[49])

with open('COLING_dataset_final/scigen_dev.json', 'rb') as f4:
    dev_json = json.loads(f4.read())

print(len(dev_json))

print(dev_json)
for i in range(len(dev_json)):
    print(i)

print(dev_json['0'])
x = list(dev_json.values())
print(len(x))
print(x[0])

for i in range(len(x)):
    




