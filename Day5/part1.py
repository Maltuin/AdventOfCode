import re

is_seed = True
mappings = {}
new_mapping = {}

for line in open("data.txt", "r"):
    if is_seed is True:
        for seed in map(lambda x: int(x), re.findall("\d+", line)):
            mappings[seed] = seed
        is_seed = False

    if is_seed is False:
        number = list(map(lambda x: int(x), re.findall("\d+", line)))
        if len(number) == 3:
            for key, value in mappings.items():
                if value >= number[1] and value < number[1] + number[2]:
                    new_mapping[key] = value - (number[1] - number[0])
        else:
            for key, value in new_mapping.items():
                mappings[key] = value
            new_mapping = {}
            
for key, value in new_mapping.items():
    mappings[key] = value

print(min(mappings.values()))