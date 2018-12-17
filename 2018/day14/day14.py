from collections import deque

rcps = [3,7]
elf1 = 0
elf2 = 1

steps = 0

l = 84601
findstr = "084601"
last_rcps = deque()
found = False
while not found:
    csum = "%s" % (rcps[elf1] + rcps[elf2])
    for c in csum:
        rcps.append(int(c))
        if len(last_rcps) >= len(findstr):
            last_rcps.popleft()
        last_rcps.append(c)
        if findstr == "".join(("%s" % r for r in last_rcps)):
            print "Part2: found %r" % (len(rcps)-len(findstr))
            found = True
            break
    elf1 = (elf1 + 1 + rcps[elf1]) % len(rcps)
    elf2 = (elf2 + 1 + rcps[elf2]) % len(rcps)

    #print rcps
    
    steps +=1
    
print "Part1 %r" % ("".join(["%s" % r for r in rcps[l:l+10]]))
