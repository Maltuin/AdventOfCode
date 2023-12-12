import re
from math import lcm

file = open("data.txt", "r")

points = {}
currentpoints = []
road = file.readline()
file.readline()

for line in file:
    datas = re.findall("\w+", line)
    if datas[0].endswith("A"):
        currentpoints.append(datas[0])
    points[datas[0]] = {"L" : datas[1], "R": datas[2]}

mod = len(road) - 1
ends = []

for point in currentpoints:
    count = 0
    
    while True:
        point = points[point][road[count%mod]]
        count += 1
        if point.endswith("Z"):
            ends.append(count)
            break

print(lcm(*ends))