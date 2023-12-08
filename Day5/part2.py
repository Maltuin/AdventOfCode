import datetime
import re

print(datetime.datetime.now())

is_seed = True
actions_list= [
    "humidity-to-location map:\n",
    "temperature-to-humidity map:\n",
    "light-to-temperature map:\n",
    "water-to-light map:\n",
    "fertilizer-to-water map:\n",
    "soil-to-fertilizer map:\n",
    "seed-to-soil map:\n"
]
seeds = []
actions = []
actionstring = "seed"

for line in open("data.txt", "r"):
    if is_seed is True:
        seeds_regex = list(map(lambda x: int(x), re.findall("\d+", line)))
        for x in range(0, len(seeds_regex) - 1, 2):
            seeds.append((seeds_regex[x], seeds_regex[x] + seeds_regex[x + 1]))
        is_seed = False
    else:
        number = re.findall("\d+", line)
        if len(number) == 3:
            number = list(map(lambda x: int(x), number))
            actions.append(
                { 
                    "action": actionstring,
                    "diff": number[1] - number[0],
                    "start": number[0],
                    "end": number[0] + number[2]
                }
            )
        else:
            actionstring = line

cont = True
current = 60556152

while cont == True:
    calcul = current
    for action in actions_list:
        for todo in filter(lambda x: x["action"] == action, actions):
            if(calcul >= todo["start"] and calcul < todo["end"]):
                calcul += todo["diff"]
                break
    for seed in seeds:
        if calcul >= seed[0] and calcul < seed[1]:
            print(current)
            cont = False
            break
    current += 1

print(datetime.datetime.now())