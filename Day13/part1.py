def get_sym(blocklines):
    for x in range(1, len(blocklines)):
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

result = 0

for block in open("data.txt", "r").read().split("\n\n"):
    blocklines = block.splitlines()
    result += get_sym(blocklines) * 100
    result += get_sym(list(zip(*blocklines)))

print(result)