import re

total = 0

REPLACE = [
  ("threeight", "38"),
  ("oneight", "18"),
  ("eightwo", "82"),
  ("nineight", "98"),
  ("twone", "21"),
  ("sevenine", "79"),
  ("eighthree", "83"),
  ("one", "1"),
  ("two", "2"),
  ("three", "3"),
  ("four", "4"),
  ("five", "5"),
  ("six", "6"),
  ("seven", "7"),
  ("eight", "8"),
  ("nine", "9")
]

f = open("data.txt","r")
text = f.read()

for old, new in REPLACE:
  text = text.replace(old, new)

for x in text.splitlines():
  result = re.findall("\d", x)
  total += int(result[0] + result[-1])

print(total)