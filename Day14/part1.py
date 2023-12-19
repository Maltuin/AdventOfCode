import re

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
    blocks = list(map(lambda x: x[0], filter(lambda x: x[0] < rolling_rock[0] and x[1] == rolling_rock[1], blocking_rocks)))
    first_blocking_rock = max(blocks) + 1 if len(blocks) > 0 else 0

    nb_rock_beetwen = len(list(filter(lambda x: x[0] < rolling_rock[0] and x[0] >= first_blocking_rock and x[1] == rolling_rock[1], rolling_rocks)))
    result += ligne  - nb_rock_beetwen - first_blocking_rock

print(result)