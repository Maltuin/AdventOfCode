import re

global blocking_rocks
global rolling_rocks

def filt_check(x, rolling_rock):
    return x[0] < rolling_rock[0] and x[1] == rolling_rock[1]

def filt_check2(x, rolling_rock, first_blocking_rock):
    return x[0] < rolling_rock[0] and x[0] >= first_blocking_rock and x[1] == rolling_rock[1]

def get_coo(file, reg):
    temp = []
    for rock in re.finditer(reg, file):
        a = divmod(rock.start(), 11)
        temp.append([a[0], a[1]])
    return temp

def get_final_line(rolling_rock):
    blocks = [item[0] for item in blocking_rocks if filt_check(item, rolling_rock)]
    first_blocking_rock = max(blocks) + 1 if len(blocks) > 0 else 0

    nb_rock_beetwen = len([item[0] for item in rolling_rocks if filt_check2(item, rolling_rock, first_blocking_rock)])
    return first_blocking_rock + nb_rock_beetwen

def load(rolling):
    temp = []
    for rolling_rock in rolling:
        temp.append([get_final_line(rolling_rock), rolling_rock[1]])
    return temp
    
file = open("data.txt", "r").read()
blocking_rocks = get_coo(file, "#").copy()
rolling_rocks = get_coo(file, "O").copy()

print(rolling_rocks)
rolling_rocks = load(rolling_rocks)
print(rolling_rocks)