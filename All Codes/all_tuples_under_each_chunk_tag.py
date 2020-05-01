import re
import json

possible_chunk_tags = ['NP', 'VGNF', 'RBP',
                       'CCP', 'VGNN', 'NEGP', 'VGF', 'JJP', 'BLK', 'VGINF']

possible_tuples = {
    "CCP": [],
    "VGNF": [],
    "NEGP": [],
    "BLK": [],
    "NP": [],
    "VGNN": [],
    "RBP": [],
    "JJP": [],
    "VGF": [],
    "VGINF": [],
}

with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/numbered.txt", "r") as f:
    for line in f:

        if line.strip():
            line = re.sub('\s+', ' ', line)
            # print(line)

            if line.split(" ")[1].strip() == "((":
                cur_tuple = []
                cur_tag = line.split("((")[1].split("<")[0].strip()

            elif line.split(" ")[1].strip() == "))":
                if cur_tag in possible_chunk_tags:
                    if cur_tuple not in possible_tuples[cur_tag]:
                        possible_tuples[cur_tag].append(cur_tuple)

            elif line[0] != '<':
                cur_tuple.append(line.split(" ")[2])

# print(possible_tuples)

with open("possible_tuples.json", "w") as fp:
    json.dump(possible_tuples, fp, indent=2)
