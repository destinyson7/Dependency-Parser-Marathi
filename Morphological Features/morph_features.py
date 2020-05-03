import re
import sys

cnt = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

total = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        if line.strip():
            current = re.sub('\s+', ' ', line)

            if current.split(" ")[0] == "<Sentence":
                pass

            elif current.strip() == "</Sentence>":
                pass

            elif current.split(" ")[1].strip() == "((":
                pass

            elif current.split(" ")[1].strip() == "))":
                pass

            else:
                try:
                    morph = current.split("af")[1].strip().split(",")
                    # print(morph)
                    total += 1

                    if morph[1].strip():
                        cnt[0] += 1

                    if morph[2].strip():
                        cnt[1] += 1

                    if morph[3].strip():
                        cnt[2] += 1

                    if morph[4].strip():
                        cnt[3] += 1

                    if morph[5].strip():
                        cnt[4] += 1

                except:
                    pass

print(cnt)
print(total)
