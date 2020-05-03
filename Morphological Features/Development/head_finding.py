import json
import re
import sys

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


with open(sys.argv[1], "r") as f:

    cur_sentence = []
    full_sentence = []
    add_sentence = []
    chunk_tag = ""
    chunk_name = ""
    words = []
    relation = ""
    parent = ""
    morph_features = {}
    sentence_id = -1
    wrong_sentences = []
    is_wrong = False
    root_found = False

    for line in f:
        if line.strip():
            current = re.sub('\s+', ' ', line)

            if current.split(" ")[0] == "<Sentence":
                cur_sentence = [current]
                sentence_id = current.split("'")[1]
                is_wrong = False
                root_found = False

            elif current.strip() == "</Sentence>":

                if is_wrong or not root_found:
                    # if not root_found:
                    #     print(cur_sentence)
                    wrong_sentences.append(sentence_id)
                else:
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
                # print(current)
                try:
                    chunk_name = current.split(
                        "((")[1].split("name")[1].split("'")[1]

                except:
                    is_wrong = True
                    chunk_name = "NOT FOUND"

                if not (current.find("drel") >= 0):
                    relation = "NULL"
                    parent = "ROOT"

                    if root_found:
                        # print(sentence_id)
                        is_wrong = True

                    root_found = True

                else:
                    try:
                        relation = current.split("drel")[1].split(
                            "'")[1].split(":")[0]
                    except:
                        # print(line)
                        is_wrong = True
                        relation = "NOT FOUND"

                    try:
                        parent = current.split("drel")[1].split("'")[1].split(
                            ":")[1]

                    except:
                        # print(line)
                        is_wrong = True
                        parent = "NOT FOUND"

            elif current.split(" ")[1].strip() == "))":
                head, head_tag = find_head_of_chunk(chunk_tag, words)
                add_sentence.append("H " + head + " " + chunk_tag + " " +
                                    head_tag + " " + chunk_name + " " + relation + " " + parent + " " + morph_features[head])

                words = []
                head_tag = ""
                chunk_tag = ""
                chunk_name = ""
                relation = ""
                parent = ""
                morph_features = {}

            else:
                word = current.split(" ")[1]
                tag = current.split(" ")[2]

                morph_features[word] = ""

                try:
                    morph = current.split("af")[1].strip().split(",")

                    fl = True

                    if morph[2].strip() and morph[2].strip() in ["m", "f", "n"]:
                        morph_features[word] += morph[2].strip() + " "

                    else:
                        morph_features[word] += "NULL "

                    if morph[2].strip() and morph[2].strip() not in ["m", "f", "n"]:
                        fl = False

                    if morph[3].strip() and morph[3].strip() in ["sg", "pl"]:
                        morph_features[word] += morph[3].strip() + " "

                    else:
                        morph_features[word] += "NULL "

                    if morph[3].strip() and morph[3].strip() not in ["sg", "pl"]:
                        fl = False

                    if morph[5].strip() and morph[5].strip() in ["d", "o"]:
                        morph_features[word] += morph[5].strip() + " "

                    else:
                        morph_features[word] += "NULL "

                    if morph[5].strip() and morph[5].strip() not in ["d", "o"]:
                        fl = False

                    if fl and morph[1].strip():
                        morph_features[word] += morph[1].strip()

                    else:
                        morph_features[word] += "NULL"

                except:
                    morph_features[word] = "NULL NULL NULL NULL"

                words.append((word, tag))
                full_sentence.append(word)

print(*sentences)

new_file = open("head_sentences.txt", "w")
new_file.writelines(sentences)
new_file.close()


# print(wrong_sentences)
# print(len(wrong_sentences))
