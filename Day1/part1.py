import re

total = 0

for x in open("data.txt", "r"):
  result = re.findall("\d", x)
  total += int(result[0] + result[-1])

print(total)