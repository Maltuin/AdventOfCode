import re
import numpy as np
col = 141

points = []

for point in re.finditer("#", open("data.txt", "r").read()):
    points.append(divmod(point.start(), col))

line = set(map(lambda x: x[0], points))
column = set(map(lambda x: x[1], points))
count = 0

for x in range(0, len(points)):
    p1x, p1y = points[x]
    for y in range(x+1, len(points)):
        p2x, p2y = points[y]
        count += abs(p2x - p1x) + abs(p2y - p1y)
        count += 999999 * len(set(np.arange(p1x, p2x)) - line)
        count += 999999 * len(set(np.arange(min([p1y, p2y]), max([p1y, p2y]))) - column)

print(count)