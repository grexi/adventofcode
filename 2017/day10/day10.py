

def knothash(length, rotates):
    ring = [x for x in range(length)]
    skip = 0
    i = 0
    for rot in rotates:
        part = []
        for j in range(rot):
            part.append(ring[(i+j)%length])
        j = 0
        for p in reversed(part):
            ring[(i+j) % length] = p
            j+=1
        i += skip+rot
        skip += 1
    return ring


def knothash_str(length, string):
    ring = [x for x in range(length)]
    skip = 0
    i = 0
    rotates = []
    for s in string:
        rotates.append(ord(s))
    rotates.extend([17, 31, 73, 47, 23])
    for _ in range(64):
        for rot in rotates:
            part = []
            for j in range(rot):
                part.append(ring[(i+j)%length])
            j = 0
            for p in reversed(part):
                ring[(i+j) % length] = p
                j+=1
            i += skip+rot
            skip += 1

    total_hash = []    
    for x in range(16):
        hashval = 0
        for y in range(16):
            hashval = hashval ^ ring[x*16+y]
        total_hash.append(hashval)        
    return "".join(["%02x" % x for x in total_hash])


day10input = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]

kh = knothash(256, day10input)
print("Part 1: %d" % (kh[0]*kh[1]))


print("Part 2: %s" % (knothash_str(256, "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243")))
