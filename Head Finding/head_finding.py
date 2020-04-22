import json

with open('/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Head Preprocessing/Marathi_Head_Finding.json') as fp:
    head_mapping = json.load(fp)

print(head_mapping)

with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/numbered.txt", "r") as f:
    for line in f:
        