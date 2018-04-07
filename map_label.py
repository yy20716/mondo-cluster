#!/usr/bin/env python

import csv

go_label_dict = {}
core_go_dict = {}

with open('go_label.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
           if row[0] == 'class': 
              continue
           prefix, body = row[0].split('_')
           go_label_dict['GO_' + body] = row[1]
        except IndexError:
           pass 

with open('core_samples.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
           if row[2] == 'name': 
              continue
           core_go_dict[row[2]] = row[1]
        except IndexError:
           pass 

for key, value in core_go_dict.items():
    try:
        print(key, value, go_label_dict[key])
    except IndexError:
        pass 
