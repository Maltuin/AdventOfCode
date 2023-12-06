import re

col = 141

f = open("data.txt","r")
text = f.read()

result = 0
symbols = []

for symbol in re.finditer("[^a-zA-Z0-9.\n]", text):
    index = divmod(symbol.start(), col)
    symbols.append((index[0], index[1]))


for number in re.finditer("\d+", text):
    start = divmod(number.start(), col)
    end = divmod(number.end(), col)
    if any((x) for x in symbols if (
        x[0] >= start[0] - 1 and
        x[0] <= start[0] + 1 and
        x[1] >= start[1] - 1 and
        x[1] < end[1] + 1
        )):
        result += int(number.group())

print(result)