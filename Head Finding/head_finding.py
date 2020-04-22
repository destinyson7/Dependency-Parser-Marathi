import json
import re

with open('./head_mapping.json') as fp:
    head_mapping = json.load(fp)

# print(head_mapping)


def find_head_of_chunk(chunk_tag, words):
    for tag in head_mapping[chunk_tag]:
        for i in range(len(words) - 1, -1, -1):
            if words[i][1] == tag:
                return words[i][0]

    assert (False)


sentences = []


def add_sentence_to_list(cur_sentence):
    for line in cur_sentence:
        sentences.append(line + "\n")


with open(
        "/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/numbered.txt",
        "r") as f:

    cur_sentence = []
    full_sentence = []
    add_sentence = []
    chunk_tag = ""
    words = []
    relation = ""
    parent = ""

    for line in f:
        if line.strip():
            current = re.sub('\s+', ' ', line)

            if current.split(" ")[0] == "<Sentence":
                cur_sentence = [current]

            elif current.strip() == "</Sentence>":
                cur_sentence.append(" ".join(full_sentence))

                for heads in add_sentence:
                    cur_sentence.append(heads)

                cur_sentence.append(current)
                add_sentence_to_list(cur_sentence)
                cur_sentence = []
                add_sentence = []
                full_sentence = []

            elif current.split(" ")[1].strip() == "((":
                chunk_tag = current.split("((")[1].split("<")[0].strip()

                if not (current.find("drel") >= 0):
                    relation = "NULL"
                    parent = "ROOT"

                else:
                    try:
                        relation = current.split("drel")[1].split(
                            "'")[1].split(":")[0]
                    except:
                        # print(line)
                        relation = "NOT FOUND"

                    try:
                        parent = current.split("drel")[1].split("'")[1].split(
                            ":")[1]

                    except:
                        # print(line)
                        parent = "NOT FOUND"

            elif current.split(" ")[1].strip() == "))":
                head = find_head_of_chunk(chunk_tag, words)
                add_sentence.append("H " + head + " " + chunk_tag + " " +
                                    relation + " " + parent)
                words = []
                chunk_tag = ""
                relation = ""
                parent = ""

            else:
                word = current.split(" ")[1]
                tag = current.split(" ")[2]
                words.append((word, tag))
                full_sentence.append(word)

print(*sentences)

new_file = open("head_sentences.txt", "w")
new_file.writelines(sentences)
new_file.close()