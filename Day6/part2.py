import re

lines = open("data.txt", "r").readlines()

duration = int(''.join(re.findall("\d+", lines[0])))
distance = int(''.join(re.findall("\d+", lines[1])))

for x in range(1, duration):
    if x * (duration - x) > distance:
        start_winning = x
        break

for x in range(duration, start_winning, -1):
    if x * (duration - x) > distance:
        end_winning = x
        break

print((end_winning - start_winning) + 1)