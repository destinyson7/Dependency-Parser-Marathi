import re

sentences = []


def add_sentence(cur_sentence):
    for line in cur_sentence:
        sentences.append(line)


with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/cleaned.txt", "r") as f:

    cur_sentence = []
    to_add = True

    for line in f:
        current = line.strip()

        # if len(current.split("((")) > 1:
        #     tag = current.split("((")[1].split("<")[0].strip()
        #     if tag in incorrect_tags or tag[:4] == "NULL":
        #         to_add = False

        if current:
            stripped_line = re.sub('\s+', ' ', line)
            temp_line = stripped_line
            temp_line = re.sub("\[\[", '', temp_line)
            temp_line = re.sub('__', '_', temp_line)
            temp_line = re.sub('_', '__', temp_line)

            if stripped_line[0] != "<" and len(stripped_line.split(" ")) > 1 and not (stripped_line.find("))") >= 0 or stripped_line.find("((") >= 0):
                temp_line = temp_line.split(" ")
                temp_line[2] = temp_line[2].upper()
                temp_line = " ".join(temp_line)

            cur_sentence.append(temp_line + "\n")

            if stripped_line.strip() == "</Sentence>":

                if to_add:
                    add_sentence(cur_sentence)

                else:
                    to_add = True

                cur_sentence = []

        else:
            sentences.append(line)

# print(*sentences)

new_file = open("more_cleaned.txt", "w")
new_file.writelines(sentences)
new_file.close()
