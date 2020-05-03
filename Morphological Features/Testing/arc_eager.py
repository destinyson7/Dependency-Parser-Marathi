import re
import sys
from collections import deque

sentences = []
non_parsable = []
non_parsable_sentences = []


def add_sentence_to_list(cur_sentence):
    for line in cur_sentence:
        sentences.append(line + "\n")


def add_sentence_to_non_parsable_list(cur_sentence):
    for line in cur_sentence:
        non_parsable_sentences.append(line + "\n")


def arc_eager(relations, stack, buffer):

    children = []

    while(len(stack) != 1 or len(buffer) != 0):
        # print(stack, buffer)

        if(len(buffer) == 0):
            if stack[-1] in children:
                # print("REDUCE")
                stack.pop()

            else:
                # print("*")
                return False

        else:

            # print(relations)
            if (stack[-1], buffer[0], "L") in relations:
                if buffer[0] not in children:
                    # print("RIGHT ARC")
                    children.append(buffer[0])
                    stack.append(buffer.popleft())

                else:
                    # print("**")
                    return False

            elif (stack[-1], buffer[0], "R") in relations:
                if stack[-1] not in children:
                    # print("LEFT ARC")
                    children.append(stack[-1])
                    stack.pop()

                else:
                    # print("***")
                    return False

            else:

                flag = False

                for i in range(len(stack) - 2, -1, -1):
                    if (stack[i], buffer[0], "L") in relations or (stack[i], buffer[0], "R") in relations:
                        if stack[-1] in children:
                            # print("REDUCE")
                            stack.pop()
                            flag = True
                            break

                if not flag:
                    # print("SHIFT")
                    stack.append(buffer.popleft())

    if len(stack) == 1 and len(buffer) == 0 and stack[-1] == "ROOT":
        return True

    else:
        return False


with open(sys.argv[1], "r") as f:

    for line in f:

        if line.strip():
            current = re.sub('\s+', ' ', line)
            current = current.strip()

            # print(current)

            if current.split(" ")[0] == "<Sentence":
                cur_sentence = []
                sentence_id = current.split("'")[1]
                cur_sentence.append(current.strip())
                relations = []
                stack = deque()
                stack.append("ROOT")

            elif current.strip() == "</Sentence>":
                if arc_eager(relations, stack, buffer):
                    cur_sentence.append(current.strip())
                    add_sentence_to_list(cur_sentence)

                else:
                    cur_sentence.append(current.strip())
                    add_sentence_to_non_parsable_list(cur_sentence)
                    non_parsable.append(sentence_id)

            elif current.split(" ")[0] == "H":
                cur_sentence.append(current.strip())
                cur_relations = current.split("*")
                relations.append((cur_relations[0].split(" ")[4].strip(), cur_relations[1].split(
                    " ")[5].strip(), cur_relations[2].split(" ")[1].strip()))

            elif current.split(" ")[0] == "CT":
                cur_sentence.append(current.strip())
                buffer = deque(current.split(" ")[1:])
                # print(buffer)

            elif current.split(" ")[0] == "ROOT":
                cur_sentence.append(current)
                relations.append(("ROOT", current.split(
                    "*")[1].split(" ")[5].strip(), "L"))

            else:
                cur_sentence.append(current.strip())

# print(*sentences)

# print(non_parsable)
# print(len(non_parsable))

print(*sentences)

new_file = open("parsable_dependency_sentences.txt", "w")
new_file.writelines(sentences)
new_file.close()

second_file = open("non_parsable_dependency_sentences.txt", "w")
second_file.writelines(non_parsable_sentences)
second_file.close()
