possible_tags = set([])

with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/numbered.txt", "r") as f:
    for line in f:
        current = line.strip()

        if len(current.split("((")) > 1:

            tag = current.split("((")[1].split("<")[0].strip()
            possible_tags.add(tag)

print(list(possible_tags))

new_file = open("possible_tags.txt", "w")
new_file.writelines([(tag + '\n') for tag in possible_tags])
new_file.close()
