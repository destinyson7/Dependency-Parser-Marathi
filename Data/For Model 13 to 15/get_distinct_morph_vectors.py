import sys
import pickle

morph_vectors = set([])

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                morph_vectors.add("ROOT")

            else:
                morph_vectors.add(
                    " ".join(current[0].strip().split(" ")[7:]).strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                morph_vectors.add("ROOT")

            else:
                morph_vectors.add(
                    " ".join(current[1].strip().split(" ")[7:]).strip())


with open(sys.argv[2], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                morph_vectors.add("ROOT")

            else:
                morph_vectors.add(
                    " ".join(current[0].strip().split(" ")[7:]).strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                morph_vectors.add("ROOT")

            else:
                morph_vectors.add(
                    " ".join(current[1].strip().split(" ")[7:]).strip())


with open(sys.argv[3], "r") as f:
    for line in f:
        if line.strip():

            current = line.split("*")

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                morph_vectors.add("ROOT")

            else:
                morph_vectors.add(
                    " ".join(current[0].strip().split(" ")[7:]).strip())

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                morph_vectors.add("ROOT")

            else:
                morph_vectors.add(
                    " ".join(current[1].strip().split(" ")[7:]).strip())

print(list(morph_vectors))
print(len(list(morph_vectors)))

with open('morph_vectors', 'wb') as fp:
    pickle.dump(list(morph_vectors), fp)

# with open('morph_vectors', 'rb') as fp:
#     morph_vectors = pickle.load(fp)
