def get_sym(blocklines, line):
    for x in range(1, len(blocklines)):
        firsthalf = blocklines[:x][::-1]
        secondhalf = blocklines[x:]
        size = min(len(firsthalf), len(secondhalf))

        same = True
        for y in range(0, size):
            if(firsthalf[y] != secondhalf[y]):
                same = False
                break

        if(same and line > x - size and line < x + size):
            return x
    
    return 0

def boucle(blocklines):
    for x in range(0, len(blocklines)):
        for y in range(0,len(blocklines[x])):
            temp = blocklines.copy()
            line = list(temp[x])
            line[y] = "." if line[y] == "#" else "#"
            temp[x] = "".join(line)

            res = get_sym(temp, x)

            if res != 0:
                return res
    return 0

result = 0

for block in open("data.txt", "r").read().split("\n\n"):
    lines = block.splitlines()
    
    hor = boucle(lines)
    
    result += hor * 100 if hor != 0 else boucle(list(map(lambda x: "".join(x), zip(*lines))))

print(result)