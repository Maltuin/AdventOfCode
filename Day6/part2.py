import re

datas = []


for line in open("data.txt", "r"):
    datas.append(int(''.join(re.findall("\d+", line))))

start_winning = 0
end_winning = 0
duration = datas[0]
distance = datas[1]

for x in range(1, duration):
    if x * (duration - x) > distance:
        start_winning = x
        break

for x in range(duration, start_winning, -1):
    if x * (duration - x) > distance:
        end_winning = x
        break

print((end_winning - start_winning) + 1)