inp = open("input.txt", "r").readlines()



def part1(inp):
    count = 0
    for l in inp:
        v = int(l)
        count += v
    return count

def part2(inp):
    freq = {}
    count = 0
    reached = False
    while not reached:
        for l in inp:
            v = int(l)
            count += v
            if count not in freq:
                freq[count] = 1
            else:
                reached = True
                break
    return count

print(part1(inp))

print(part2(inp))