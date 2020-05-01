import sys
import pickle


chunk_tags = set([])

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                chunk_tags.add("ROOT")

            else:
                chunk_tags.add(current[0].strip().split(" ")[3].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                chunk_tags.add("ROOT")

            else:
                chunk_tags.add(current[1].strip().split(" ")[3].strip())


with open(sys.argv[2], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                chunk_tags.add("ROOT")

            else:
                chunk_tags.add(current[0].strip().split(" ")[3].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                chunk_tags.add("ROOT")

            else:
                chunk_tags.add(current[1].strip().split(" ")[3].strip())

with open(sys.argv[3], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                chunk_tags.add("ROOT")

            else:
                chunk_tags.add(current[0].strip().split(" ")[3].strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                chunk_tags.add("ROOT")

            else:
                chunk_tags.add(current[1].strip().split(" ")[3].strip())

print(list(chunk_tags))
print(len(list(chunk_tags)))

with open('chunk_tags', 'wb') as fp:
    pickle.dump(list(chunk_tags), fp)

# with open('chunk_tags', 'rb') as fp:
#     words = pickle.load(fp)
