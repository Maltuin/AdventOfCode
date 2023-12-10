import re
file = open("data.txt", "r")

points = {}
starts = []
road = file.readline()
file.readline()

for line in file:
    datas = re.findall("\w+", line)
    if datas[0].endswith("A"):
        starts.append(datas[0])
    points[datas[0]] = {"L" : datas[1], "R": datas[2]}

mod = len(road) - 1
count = 0
starts = "AAA"

while point != "ZZZ":
    point = points[point][road[count%mod]]
    count += 1

print(count)