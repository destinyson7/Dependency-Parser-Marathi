import pickle
import sys
from itertools import repeat
from scipy.sparse import csr_matrix
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import numpy as np

with open('../../words', 'rb') as fp:
    words = pickle.load(fp)

# with open('../../pos_tags', 'rb') as fp:
#     pos_tags = pickle.load(fp)

# with open('../../chunk_tags', 'rb') as fp:
#     chunk_tags = pickle.load(fp)

# print(words)
# print(pos_tags)
# print(chunk_tags)

N = len(words) + \
    len(words)

Y = []
classes = set([])

words_len = len(words)
# pos_len = len(pos_tags)
# chunk_len = len(chunk_tags)

row_ind = []
col_ind = []

word_index = {}
# pos_index = {}
# chunk_index = {}

for i in range(len(words)):
    word_index[words[i]] = i

# for i in range(len(pos_tags)):
#     pos_index[pos_tags[i]] = i

# for i in range(len(chunk_tags)):
#     chunk_index[chunk_tags[i]] = i


with open(sys.argv[1], "r") as f:
    for line in f:
        if line.strip():
            current = line.strip().split("*")

            # print(len(Y))

            if current[0].strip().split(" ")[0].strip() == "ROOT":
                col_ind.append(word_index["ROOT"])
                # col_ind.append(words_len + pos_index["ROOT"])
                # col_ind.append(words_len + pos_len + chunk_index["ROOT"])

            else:
                # print(current[0].strip().split(" ")[1])
                col_ind.append(word_index[(current[0].strip().split(" ")[1])])
                # col_ind.append(
                #     words_len + pos_index[(current[0].strip().split(" ")[2])])
                # col_ind.append(words_len + pos_len +
                #                chunk_index[(current[0].strip().split(" ")[3])])

            if current[1].strip().split(" ")[0].strip() == "ROOT":
                col_ind.append(words_len + word_index[("ROOT")])
                # col_ind.append(words_len + pos_tags.index("ROOT"))
                # col_ind.append(words_len + pos_len + chunk_tags.index("ROOT"))

            else:
                # print(current[1].strip().split(" ")[1])
                col_ind.append(
                    words_len + word_index[(current[1].strip().split(" ")[1])])
                # col_ind.append(words_len + pos_len + chunk_len + words_len +
                #                pos_index[(current[1].strip().split(" ")[2])])
                # col_ind.append(words_len + pos_len + chunk_len + words_len +
                #                pos_len + chunk_index[(current[1].strip().split(" ")[3])])

            row_ind.extend(repeat(len(Y), 2))

            Y.append(current[3].strip())
            classes.add(current[3].strip())

M = len(Y)
data = [1] * len(col_ind)

# print(col_ind)

# print(len(Y))
# print(len(row_ind))
# print(len(col_ind))
# print(len(data))

X = csr_matrix((data, (row_ind, col_ind)), shape=(M, N))
# print(np.shape(X))

SVM = pickle.load(open('SVM.sav', 'rb'))
Y_svm = SVM.predict(X)
print(Y_svm)

print()
print()
print()
print()

logisticRegr = pickle.load(open('LogisticRegression.sav', 'rb'))
Y_logisticRegr = logisticRegr.predict(X)
print(Y_logisticRegr)

print()
print()
print()
print()

score_SVM = SVM.score(X, Y)
print(score_SVM * 100)

score_LR = logisticRegr.score(X, Y)
print(score_LR * 100)

# print(Y == Y_svm)
# print(Y == Y_logisticRegr)
