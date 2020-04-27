import re

sentences = []


def add_sentence_to_list(cur_sentence):
    for line in cur_sentence:
        sentences.append(line + "\n")


def find_dependencies(heads):

    cur_sentence = []
    chunk_tags = "CT "

    pos1 = 0

    for head in heads:
        chunk_tags += head.split(" ")[4].strip() + " "

        if head.split(" ")[-1].strip() != "ROOT":

            parent = head.split(" ")[-1].strip()
            pos2 = 0

            for h in heads:
                # print(head, "***", h)
                if h.split(" ")[-3].strip() == parent:
                    # print("OKAYYYY")

                    add = (head.strip() if pos1 < pos2 else h.strip()) + " * " + (h.strip() if pos1 <
                                                                                  pos2 else head.strip()) + " * " + ("R" if pos1 < pos2 else "L") + " * " + head.split(" ")[-2].strip()
                    cur_sentence.append(add)
                    break

                pos2 += 1
        else:
            add = "ROOT" + " * " + head.strip() + " * " + "L" + " * " + "ROOT"
            cur_sentence.append(add)

        pos1 += 1

    return cur_sentence, chunk_tags


with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Head Finding/head_sentences.txt", "r") as f:

    for line in f:
        if line.strip():
            current = re.sub('\s+', ' ', line)

            if current.split(" ")[0] == "<Sentence":
                sentences.append(current + "\n")
                heads = []

            elif current.strip() == "</Sentence>":
                cur_sentence, chunk_tags = find_dependencies(heads)
                sentences.append(chunk_tags + "\n")
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
