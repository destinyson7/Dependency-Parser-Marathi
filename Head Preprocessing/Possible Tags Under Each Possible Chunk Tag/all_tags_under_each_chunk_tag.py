import re
import json

possible_chunk_tags = ['FRAGP', 'RBPP', 'RB', 'CCP', 'VGNF', 'NEGP', 'RP', 'BLK',
                       'NP', 'UNK', 'VGJJ', 'JJ', 'VGNN', 'RBP', 'JJP', 'CCPP', 'VGF', 'BL', 'VGINF', 'VNF']

possible_tags = {
    "FRAGP": set([]),
    "RBPP": set([]),
    "RB": set([]),
    "CCP": set([]),
    "VGNF": set([]),
    "NEGP": set([]),
    "RP": set([]),
    "BLK": set([]),
    "NP": set([]),
    "UNK": set([]),
    "VGJJ": set([]),
    "JJ": set([]),
    "VGNN": set([]),
    "RBP": set([]),
    "JJP": set([]),
    "CCPP": set([]),
    "VGF": set([]),
    "BL": set([]),
    "VGINF": set([]),
    "VNF": set([]),
}

with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/combined.txt", "r") as f:
    for line in f:

        if line.strip():
            line = re.sub('\s+', ' ', line)
            # print(line)

            if line.split(" ")[1].strip() == "((":
                cur_tag = line.split("((")[1].split("<")[0].strip()

            elif line.split(" ")[1].strip() == "))":
                continue

            elif line[0] != '<':
                if cur_tag in possible_chunk_tags:
                    possible_tags[cur_tag].add(line.split(" ")[2])

print(possible_tags)


class SetEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, set):
            return list(obj)

        return json.JSONEncoder.default(self, obj)


with open("possible_tags_under_each_chunk_tag.json", "w") as fp:
    json.dump(possible_tags, fp, indent=2, cls=SetEncoder)
