def get_sym(blocklines):
    for x in range(1, len(blocklines) -1):
        firsthalf = blocklines[:x][::-1]
        secondhalf = blocklines[x:]

        same = True
        for y in range(0, min(len(firsthalf), len(secondhalf))):
            if(firsthalf[y] != secondhalf[y]):
                same = False
                break

        if(same):
            return x
    
    return 0

def boucle(blocklines):
    for x in range(0, len(blocklines)):
        for y in range(0,len(blocklines[x])):
            temp = blocklines.copy()
            line = list(temp[x])
            line[y] = "." if line[y] == "#" else "#"
            temp[x] = "".join(line)
            hor = get_sym(temp)
            if hor != 0:
                return hor * 100

            ver = get_sym(list(zip(*temp)))
            if ver != 0:
                return ver
    return 0

result = 0

for block in open("data.txt", "r").read().split("\n\n"):
    result += boucle(block.splitlines())

print(result)