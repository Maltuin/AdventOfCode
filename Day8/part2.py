import re
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
count = 0

while not all(list(map(lambda x: x.endswith("Z"), currentpoints))):
    for i, cur in enumerate(currentpoints):
        currentpoints[i] = points[cur][road[count%mod]]
    count += 1
        
print(count)