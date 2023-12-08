import re

datas = []
result = 1

for line in open("data.txt", "r"):
    datas.append(list(map(lambda x: int(x), re.findall("\d+", line))))



for x in range(0, len(datas[0])):
    duration = datas[0][x]
    distance = datas[1][x]
    start_winning = 0
    end_winning = 0

    for x in range(1, duration):
        if x * (duration - x) > distance:
            start_winning = x
            break

    for x in range(duration, start_winning, -1):
        if x * (duration - x) > distance:
            end_winning = x
            break
    result *= (end_winning - start_winning) + 1

print(result)