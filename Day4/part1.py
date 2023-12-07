import re
import numpy as np 

total = 0

regex = "\d+(?![\d+:])"

for line in open("data.txt", "r"):
    numbers = line.split("|")
    a = np.intersect1d(np.array(re.findall(regex, numbers[0])), np.array(re.findall(regex, numbers[1])))
    length = len(a)
    if(length > 0):
        total += 2**(length - 1)

print(total)