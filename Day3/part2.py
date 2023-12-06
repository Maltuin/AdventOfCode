import re

col = 141

f = open("data.txt","r")
text = f.read()

result = 0
numbers = []

for number in re.finditer("\d+", text):
    start = divmod(number.start(), col)
    end = divmod(number.end(), col)
    numbers.append((start[0], start[1], end[0], end[1], number.group()))

for number in re.finditer("\*", text):
    symbol = divmod(number.start(), col)
    filtered_number = [(x) for x in numbers if (
            ((symbol[0] >= x[0] - 1 and symbol[0] <= x[0] + 1) or
            (symbol[0] >= x[2] - 1 and symbol[0] < x[2] + 1)) and
            ((symbol[1] >= x[1] - 1 and symbol[1] <= x[1] + 1) or
            (symbol[1] >= x[3] - 1 and symbol[1] < x[3] + 1))
        )]
    if len(filtered_number) == 2:
        result += int(filtered_number[0][4]) * int(filtered_number[1][4])

print(result)