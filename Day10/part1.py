import re
from math import ceil

def south(x, y):
    return (x+1, y, "south")
def north(x, y):
    return (x-1, y, "north")
def east(x, y):
    return (x, y + 1, "east")
def west(x, y):
    return (x, y - 1, "west")

start = [east, south, west, north]
data = {
    "|" : { "north" :  north, "south" : south },
    "-" : { "east" : east, "west" : west },
    "L" : { "south" : east, "west": north },
    "J" : { "south" : west, "east": north },
    "7" : { "east" : south,  "north" : west },
    "F" : { "north" : east, "west": south }
}

line = 141
text = open("data.txt", "r").read()
primalx, primaly = divmod(re.search("S", text).start(), line)

x, y, last_orientation = north(primalx, primaly)
count = 0
error = 0

while True:
    count += 1
    sign = text[(x*line) + y]

    if sign == "S":
        break
    
    try:
        x, y, last_orientation = data[sign][last_orientation](x, y)
    except KeyError:
        count = 0
        error += 1
        x,y,last_orientation = start[error](primalx, primaly)

print(ceil(count/2))