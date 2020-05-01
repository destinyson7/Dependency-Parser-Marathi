import os

data = []


def parse(f):
    for line in f:
        if line.strip() != "</document>" and line.strip() != "<document id=\"\">" and line.strip() != "<head>" and line.strip() != "</head>":
            data.append(line)


for filename in os.listdir("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/Agriculture"):
    with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/Agriculture/" + filename, "r") as f:
        parse(f)

for filename in os.listdir("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/General"):
    with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/General/" + filename, "r") as f:
        parse(f)

for filename in os.listdir("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/Grammar"):
    with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/Grammar/" + filename, "r") as f:
        parse(f)

for filename in os.listdir("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/Tourism-Parallel"):
    with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Marathi/Data/Development/Tourism-Parallel/" + filename, "r") as f:
        parse(f)

new_file = open("combined.txt", "w")
new_file.writelines(data)
new_file.close()
