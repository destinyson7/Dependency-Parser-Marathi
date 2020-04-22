import json
import re

sentences = []
removed_sentences = []


def add_sentence(cur_sentence, ):
    for line in cur_sentence:
        sentences.append(line + "\n")


def remove_sentence(cur_sentence):
    for line in cur_sentence:
        removed_sentences.append(line + "\n")


with open(
        '/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Head Preprocessing/Removing Wrongly Chunked Sentences/head_mapping.json'
) as fp:
    head_mapping = json.load(fp)

# print(head_mapping)

with open(
        "/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/more_cleaned.txt",
        "r") as f:

    to_add_sentence = True
    cur_sentence = []
    chunk_tag = ""

    for line in f:
        if line.strip():
            current = re.sub('\s+', ' ', line)

            cur_sentence.append(current)

            if current.split(" ")[0] == "<Sentence":
                cur_sentence = [current]
                to_add = False

            elif current.strip() == "</Sentence>":

                if to_add_sentence:
                    add_sentence(cur_sentence)

                else:
                    remove_sentence(cur_sentence)
                    to_add_sentence = True

                cur_sentence = []

            elif current.split(" ")[1].strip() == "((":
                chunk_tag = current.split("((")[1].split("<")[0]
                chunk_tag = chunk_tag.strip()

            elif current.split(" ")[1].strip() == "))":
                if not to_add:
                    to_add_sentence = False

                chunk_tag = ""
                to_add = False

            else:
                tag = current.split(" ")[2]

                if tag in head_mapping[chunk_tag]:
                    to_add = True

        else:
            sentences.append(line)

new_file = open("correct_sentences.txt", "w")
new_file.writelines(sentences)
new_file.close()

second_file = open("removed_sentences.txt", "w")
second_file.writelines(removed_sentences)
second_file.close()