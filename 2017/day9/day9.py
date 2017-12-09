
def parse(ex):
    garbage = False
    grouplevel = 0
    groupsum = 0
    ignorenext = False
    garbagesum = 0
    for c in ex:
        #print("%s %s %s %s %s " % (c, garbage, grouplevel, groupsum, ignorenext))
        if ignorenext:
            ignorenext = False
            continue
        if garbage:
            if c == '!':
                ignorenext = True
            elif c != '>':
                garbagesum += 1
                continue

        if c == '{':
            grouplevel += 1
            groupsum += grouplevel
        elif c == '}':
            grouplevel -= 1

        elif c == '<':
            garbage = True
        elif c == '>' and garbage:
            garbage = False
    return groupsum, garbagesum



print(parse("{{{},{},{{}}}}"))
print(parse(open("input.txt", "r").read()))
