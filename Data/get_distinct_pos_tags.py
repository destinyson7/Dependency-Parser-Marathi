import sys
import pickle


pos_tags = set([])

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                pos_tags.add("ROOT")

            else:
                pos_tags.add(current[0].strip().split(" ")[2].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                pos_tags.add("ROOT")

            else:
                pos_tags.add(current[1].strip().split(" ")[2].strip())


with open(sys.argv[2], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                pos_tags.add("ROOT")

            else:
                pos_tags.add(current[0].strip().split(" ")[2].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                pos_tags.add("ROOT")

            else:
                pos_tags.add(current[1].strip().split(" ")[2].strip())

with open(sys.argv[3], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                pos_tags.add("ROOT")

            else:
                pos_tags.add(current[0].strip().split(" ")[2].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                pos_tags.add("ROOT")

            else:
                pos_tags.add(current[1].strip().split(" ")[2].strip())

print(list(pos_tags))
print(len(list(pos_tags)))

with open('pos_tags', 'wb') as fp:
    pickle.dump(list(pos_tags), fp)

# with open('pos_tags', 'rb') as fp:
#     pos_tags = pickle.load(fp)
