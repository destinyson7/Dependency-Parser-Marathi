import re
import random

sentences = []


def add_sentence_to_list(cur_sentence):
    for line in cur_sentence:
        sentences.append(line + "\n")


def construct_pairs(num):
    all_pairs = set([])

    for i in range(num):
        for j in range(i+1, num):
            all_pairs.add((i, j))

    return all_pairs


def get_random_pairs(num_of_pairs, unrelated_pairs, indexes):
    ret = []

    sampling = random.sample(list(unrelated_pairs), k=num_of_pairs)

    for pair in sampling:
        ran = random.choice([0, 1])
        if ran == 0:
            add = indexes[pair[0]] + " * " + \
                indexes[pair[1]] + " * " + "U" + " * " + "NULL"

        else:
            add = indexes[pair[1]] + " * " + \
                indexes[pair[0]] + " * " + "U" + " * " + "NULL"

        ret.append(add)

    # print(*ret, sep="\n")
    return ret


with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Arc Eager/parsable_dependency_sentences.txt", "r") as f:

    for line in f:

        if line.strip():
            current = re.sub('\s+', ' ', line)
            current = current.strip()

            # print(current)

            if current.split(" ")[0] == "<Sentence":
                # cur_sentence = [current]
                cur_sentence = []
                indexes = []
                related_pairs = set([])
                cnt_L = 0
                cnt_R = 0

            elif current.strip() == "</Sentence>":
                all_pairs = construct_pairs(len(indexes))
                # print(len(indexes))

                unrelated_pairs = all_pairs - related_pairs

                random_number_of_pairs = min(len(unrelated_pairs), (len(
                    indexes)//random.choice([6, 7, 8])) + max(cnt_L, cnt_R), cnt_L + cnt_R)

                # print(cnt_L, cnt_R, random_number_of_pairs)

                random_pairs = get_random_pairs(
                    random_number_of_pairs, unrelated_pairs, indexes)

                cur_sentence += random_pairs
                # cur_sentence.append(current.strip())

                random.shuffle(cur_sentence)

                add_sentence_to_list(cur_sentence)

            elif current.split(" ")[0] == "H":
                cur_sentence.append(current.strip())
                cur_relations = current.split("*")
                if cur_relations[0].strip() not in indexes:
                    indexes.append(cur_relations[0].strip())

                if cur_relations[1].strip() not in indexes:
                    indexes.append(cur_relations[1].strip())

                first_index = indexes.index(cur_relations[0].strip())
                second_index = indexes.index(cur_relations[1].strip())

                related_pairs.add(
                    (min(first_index, second_index), max(first_index, second_index)))

                if cur_relations[2].strip() == "L":
                    cnt_L += 1

                else:
                    cnt_R += 1

            elif current.split(" ")[0] == "CT":
                # cur_sentence.append(current.strip())
                pass

            elif current.split(" ")[0] == "ROOT":
                cur_sentence.append(current.strip())
                cur_relations = current.split("*")

                if "ROOT" not in indexes:
                    indexes.append("ROOT")

                if cur_relations[1].strip() not in indexes:
                    indexes.append(cur_relations[1].strip())

                first_index = indexes.index("ROOT")
                second_index = indexes.index(cur_relations[1].strip())

                related_pairs.add(
                    (min(first_index, second_index), max(first_index, second_index)))

            else:
                # cur_sentence.append(current.strip())
                pass
# print(*sentences)

# print(non_parsable)
# print(len(non_parsable))

print(*sentences)

new_file = open("parsable_dependency_sentences_with_unrelated_pairs.txt", "w")
new_file.writelines(sentences)
new_file.close()
