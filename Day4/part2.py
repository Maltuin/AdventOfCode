import re
import numpy as np 

results = np.ones((188,), dtype=int)
regex = "\d+(?![\d+:])"

count = 0

for line in open("data.txt", "r"):
    numbers = line.split("|")
    length = len(np.intersect1d(np.array(re.findall(regex, numbers[0])), np.array(re.findall(regex, numbers[1]))))
    for x in range(length):
        results[x + count + 1] += results[count]
    count += 1

print(np.array(results).sum())
