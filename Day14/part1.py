import re

def count_block(blocks, rolling_rock, index):
    return [item[0] for item in blocks if filt_check(item, rolling_rock, index)]

def filt_check(x, rolling_rock, first_blocking_rock):
    return x[0] < rolling_rock[0] and x[0] >= first_blocking_rock and x[1] == rolling_rock[1]

file = open("data.txt", "r").read()
col = 101
ligne = 100

rolling_rocks = []
blocking_rocks = []

for rock in re.finditer("O", file):
    rolling_rocks.append(divmod(rock.start(), col))

for rock in re.finditer("#", file):
    blocking_rocks.append(divmod(rock.start(), col))

result = 0
for rolling_rock in rolling_rocks:
    blocks = count_block(blocking_rocks, rolling_rock, 0)
    first_blocking_rock = max(blocks) + 1 if len(blocks) > 0 else 0

    nb_rock_beetwen = len(count_block(rolling_rocks, rolling_rock, first_blocking_rock))
    result += ligne - (first_blocking_rock + nb_rock_beetwen)

print(result)