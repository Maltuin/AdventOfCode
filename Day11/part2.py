import re
import numpy as np
col = 141

points = []
line = []
column = []

for point in re.finditer("#", open("data.txt", "r").read()):
    data = divmod(point.start(), col)
    line.append(data[0])
    column.append(data[1])
    points.append([data[0], data[1]])

line = set(np.unique(line))
column = set(np.unique(column))
count = 0
points2 = points.copy()
lines = []

for point1 in points:
    points2.remove(point1)
    p1x, p1y = point1
    for point2 in points2:
        p2x, p2y = point2
        count += p2x - p1x if p2x > p1x else p1x - p2x
        count += p2y - p1y if p2y > p1y else p1y - p2y
        start = p1x if p1x < p2x else p2x
        end = p1x if p1x > p2x else p2x
        count += 999999 * len(set(np.arange(start, end, 1, dtype=int)) - line)
        start = p1y if p1y < p2y else p2y
        end = p1y if p1y > p2y else p2y
        count += 999999 * len(set(np.arange(start, end, 1, dtype=int)) - column)

    
print(count)