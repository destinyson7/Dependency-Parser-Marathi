import json
import re

with open('./head_mapping.json') as fp:
    head_mapping = json.load(fp)

# print(head_mapping)


def find_head_of_chunk(chunk_tag, words):
    for tag in head_mapping[chunk_tag]:
        for i in range(len(words) - 1, -1, -1):
            if words[i][1] == tag:
                return words[i][0], words[i][1]

    assert (False)


sentences = []


def add_sentence_to_list(cur_sentence):
    for line in cur_sentence:
        sentences.append(line + "\n")


def find_dependencies(heads):

    cur_sentence = []

    pos1 = 0

    for head in heads:
        if head.split(" ")[-1].strip() != "ROOT":

            parent = head.split(" ")[-1].strip()
            pos2 = 0

            for h in heads:
                # print(head, "***", h)
                if h.split(" ")[-3].strip() == parent:
                    # print("OKAYYYY")
                    add = head.strip() + " * " + h.strip() + " * " + \
                        ("R" if pos1 < pos2 else "L") + \
                        " * " + head.split(" ")[-2].strip()
                    cur_sentence.append(add)
                    break

                pos2 += 1
        else:
            add = "ROOT" + " * " + head.strip() + " * " + "L" + " * " + "ROOT"
            cur_sentence.append(add)

        pos1 += 1

    return cur_sentence


with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Head Finding/head_sentences.txt", "r") as f:

    for line in f:
        if line.strip():
            current = re.sub('\s+', ' ', line)

            if current.split(" ")[0] == "<Sentence":
                sentences.append(current + "\n")
                heads = []

            elif current.strip() == "</Sentence>":
                cur_sentence = find_dependencies(heads)
                add_sentence_to_list(cur_sentence)
                sentences.append(current + "\n")

            elif current[0] == "H":
                heads.append(line)

            else:
                sentence = current
                sentences.append(current + "\n")

print(*sentences)

new_file = open("dependency_sentences.txt", "w")
new_file.writelines(sentences)
new_file.close()
