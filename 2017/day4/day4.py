def is_valid(line):
    line = line.strip()
    parts = line.split()
    d = {}
    for p in parts:
        if p in d:
            return False
        d[p] = 1
    return True

def is_valid_anagram(line):
    line = line.strip()
    parts = line.split()
    d = {}
    for p in parts:
        r = "".join(sorted(p))
        if p in d:
            return False
        if r in d:
            return False
        

        d[p] = 1
        d[r] = 1
    return True


lines = open("input.txt", "r").readlines()
cnt = 0
cnt_anagram = 0
for l in lines:
    if is_valid(l):
        cnt += 1
    if is_valid_anagram(l):
        cnt_anagram += 1

print(" %d valid" % (cnt))
print(" %d valid with anagram" % (cnt_anagram))
