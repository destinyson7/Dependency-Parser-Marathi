import sys
import pickle


words = set([])

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                words.add("ROOT")

            else:
                words.add(current[0].strip().split(" ")[1].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                words.add("ROOT")

            else:
                words.add(current[1].strip().split(" ")[1].strip())


with open(sys.argv[2], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                words.add("ROOT")

            else:
                words.add(current[0].strip().split(" ")[1].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                words.add("ROOT")

            else:
                words.add(current[1].strip().split(" ")[1].strip())

with open(sys.argv[3], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                words.add("ROOT")

            else:
                words.add(current[0].strip().split(" ")[1].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                words.add("ROOT")

            else:
                words.add(current[1].strip().split(" ")[1].strip())

print(len(list(words)))

with open('words', 'wb') as fp:
    pickle.dump(list(words), fp)

# with open('words', 'rb') as fp:
#     words = pickle.load(fp)
