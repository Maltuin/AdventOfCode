import datetime
import re

is_seed = True
mappings = {}
new_mapping = {}

print(datetime.datetime.utcnow())
for line in open("data.txt", "r"):
    if is_seed is True:
        seeds = re.findall("\d+", line)
        seeds = list(map(lambda x: int(x), seeds))
        for x in (0, len(seeds) - 2):
            for y in range(seeds[x], seeds[x] + seeds[x+1]):
                mappings[y] = y
            x += 1
        is_seed = False

    if is_seed is False:
        number = re.findall("\d+", line)
        if len(number) == 3:
            number = list(map(lambda x: int(x), number))
            start = number[1]
            end = number[1] + number[2]
            diff = number[1] - number[0]
            for key, value in mappings.items():
                if value >= start and value < end:
                    new_mapping[key] = value - diff
        else:
            for key, value in new_mapping.items():
                mappings[key] = value
            new_mapping = {}
            
for key, value in new_mapping.items():
    mappings[key] = value

print(datetime.datetime.utcnow())
print(min(mappings.values()))