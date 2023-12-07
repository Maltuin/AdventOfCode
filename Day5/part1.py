import re

is_seed = True
mappings = {}
new_mapping = {}

for line in open("data.txt", "r"):
    if is_seed is True:
        seeds = re.findall("\d+", line)
        for seed in seeds:
            mappings[seed] = int(seed)
        is_seed = False

    if is_seed is False:
        number = re.findall("\d+", line)
        if len(number) == 3:
            start = int(number[1])
            end = int(number[1]) + int(number[2])
            diff = int(number[1]) - int(number[0])
            for key, value in mappings.items():
                if value >= start and value < end:
                    new_mapping[key] = value - diff
        else:
            for key, value in new_mapping.items():
                mappings[key] = value
            new_mapping = {}
            
for key, value in new_mapping.items():
    mappings[key] = value

                
print(min(mappings.values()))