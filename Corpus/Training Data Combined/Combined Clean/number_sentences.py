import re

sentence_number = 0

sentences = []

with open("/home/laaaad/IIIT-H/Courses/Semester4/Intoduction to NLP/Project/Dependency-Parser-Marathi/Corpus/Training Data Combined/Combined Clean/more_cleaned.txt", "r") as f:
    for line in f:
        stripped_line = re.sub('\s+', ' ', line)

        if stripped_line:
            if stripped_line.split(" ")[0] == "<Sentence":
                sentence_number += 1

                sentences.append("<Sentence id='" +
                                 str(sentence_number) + "'>\n")

            else:
                sentences.append(line)

        else:
            sentences.append(line)

new_file = open("numbered.txt", "w")
new_file.writelines(sentences)
new_file.close()
