import re

def get_max(color):
    return max(list(map(int, re.findall("\d+", ' '.join(re.findall("\d+ " + color, games))))), default=0)

ruleRed = 12
ruleGreen = 13
ruleBlue = 14

result = 0

for x in open("data.txt", "r"):
    line = x.split(":")
    id = re.findall("\d+", line[0])[0]
    games = line[1]

    result += get_max("red") * get_max("green") * get_max("blue")

print(result)