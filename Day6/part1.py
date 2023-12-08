import re

result = 1

lines = open("data.txt", "r").readlines()

durations = list(map(lambda x: int(x), re.findall("\d+", lines[0])))
distances = list(map(lambda x: int(x), re.findall("\d+", lines[1])))

for x in range(0, len(durations)):
    duration = durations[x]
    distance = distances[x]
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