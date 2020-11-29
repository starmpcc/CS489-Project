import csv
import json
import os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
files = os.listdir()
for csv_f in files:
    if ('tsv' in csv_f):
        csvfile = open(csv_f, 'r', encoding='utf-8')
        filename = csv_f.split('.')[0] + '.json'
        json_f = open(os.path.join('json', filename), 'w')
        obj = {}
        for l in csvfile.readlines():
            l = l.strip().split('\t')
            obj[l[0]] = l[1:]
        json.dump(obj, json_f, indent=2)
