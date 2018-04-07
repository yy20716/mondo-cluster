#!/usr/bin/env python

import csv

class mdict(dict):
    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)

new_dist_list = []
mondogo_dict = {}
mondo_dist_dict = mdict()
go_dist_dict = mdict()

thefile = open('go_dist_only.csv', 'w')

with open('mondo-leaves-to-go.tsv', 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        try:
           go_str = row[3].replace("GO:","http://purl.obolibrary.org/obo/GO_")
           mondogo_dict[row[1]] = go_str
        except IndexError:
           pass 

with open('go_dist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
           if row[0] == 'super': 
              continue
           # new_dist_list.append(row[0] + "," + row[1] + "," + row[2])
           # new_dist_list.append(row[1] + "," + row[0] + "," + row[2])
           go_dist_dict[row[0]] = [row[1], row[2]]
           go_dist_dict[row[1]] = [row[0], row[2]]
        except IndexError:
           pass 

with open('mondo_dist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
           if row[0] == 'super': 
              continue
           # new_dist_list.append(row[0] + "," + row[1] + "," + row[2])
           # new_dist_list.append(row[1] + "," + row[0] + "," + row[2])
           mondo_dist_dict[row[0]] = [row[1], row[2]]
           mondo_dist_dict[row[1]] = [row[0], row[2]]
        except IndexError:
           pass 

for key, value in mondogo_dict.items():
    try:
        mapped_gos = go_dist_dict[value]
        for each_go in mapped_gos:
           new_dist_list.append(value + "," + each_go[0] + "," + each_go[1])
           new_dist_list.append(each_go[0] + "," + value + "," + each_go[1])
        # print(key, value)
        # print(mondo_dist_dict[key])
        # print(go_dist_dict[value])
        # new_dist_list.append(key + "," + value + ",0")
        # new_dist_list.append(value + "," + key + ",0")
        # for each_mondo in mondo_dist_dict[key]:
        #   for each_go in go_dist_dict[value]:
        #      dist_sum = int(each_mondo[1]) + int(each_go[1])
        #      new_dist_list.append(each_mondo[0] + "," + each_go[0] + "," + str(dist_sum)) 
        #      new_dist_list.append(each_go[0] + "," + each_mondo[0] + "," + str(dist_sum)) 
    except Exception:
        pass

for item in new_dist_list:
    thefile.write("%s\n" % item)
