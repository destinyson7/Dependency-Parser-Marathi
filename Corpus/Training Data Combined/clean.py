import re

incorrect_tags = ["RBPP", "RB", "RP", "UNK",
                  "CCPP", "VGJJ", "BL", "VNF", "FRAGP"]

sentences = []


def add_sentence(cur_sentence):
    for line in cur_sentence:
        sentences.append(line)


with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/combined.txt", "r") as f:

    cur_sentence = []
    to_add = True

    for line in f:
        current = line.strip()

        if len(current.split("((")) > 1:

            tag = current.split("((")[1].split("<")[0].strip()
            if tag in incorrect_tags:
                to_add = False

        if current:
            stripped_line = re.sub('\s+', ' ', line)

            cur_sentence.append(line)

            if stripped_line.strip() == "</Sentence>":

                if to_add:
                    add_sentence(cur_sentence)

                else:
                    to_add = True

                cur_sentence = []

        else:
            sentences.append(line)

# print(sentences)

new_file = open("cleaned.txt", "w")
new_file.writelines(sentences)
new_file.close()
