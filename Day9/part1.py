import re

def calculate(numbers):
    temp = []

    for x in range(0, len(numbers) - 1, 1):
        temp.append(numbers[x + 1] - numbers[x])

    if not all(list(map(lambda x: x == 0, temp))):
        return numbers[-1] + calculate(temp)
    else:
        return numbers[-1]

total = 0

for line in open("data.txt", "r"):
    numbers = list(map(lambda x: int(x), re.findall("-?\d+", line)))
    total += calculate(numbers)

print(total)