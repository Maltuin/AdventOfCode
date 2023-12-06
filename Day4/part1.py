import re
import numpy as np 

total = 0

for x in open("data.txt", "r"):
    first_split = x.split(":")
    numbers = first_split[1].split("|")
    a = np.intersect1d(np.array(re.findall("\d+", numbers[0])), np.array(re.findall("\d+", numbers[1])))
    length = len(a)
    if length == 1:
        total += 1
    if length > 1:
        total += 2**(length - 1)

print(total)