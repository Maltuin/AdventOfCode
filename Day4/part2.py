import re
import numpy as np 

results = np.ones((188,), dtype=int)
count = 0

for x in open("data.txt", "r"):
    first_split = x.split(":")
    numbers = first_split[1].split("|")
    length = len(np.intersect1d(np.array(re.findall("\d+", numbers[0])), np.array(re.findall("\d+", numbers[1]))))
    for x in range(length):
        results[x + count + 1] += results[count]
    count += 1

print(np.array(results).sum())
