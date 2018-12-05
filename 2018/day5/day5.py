inp = [ord(x) for x in open("input.txt", "r").read()]

#inp = [ord(x) for x in "dabAcCaCBAcCcaDA"]

def reduce_polymer(inp):
    #print("###################################")
    idx = 0
    delidx = []
    tlen = len(inp)-1
    while idx < tlen:
        #print("Comparing %r with %r" % (chr(inp[idx]), chr(inp[idx+1])))
        diff = inp[idx] - inp[idx+1]
        if diff == 32 or diff == -32:
            #print("Match! %r %r %r" % (chr(inp[idx]), chr(inp[idx+1]), idx))
            #del inp[idx:idx+2]
            delidx.append(idx)
            idx += 2
        else:
            idx += 1
    #print inp
    for didx in reversed(delidx):
        del inp[didx:didx+2]
    #print inp
    return inp

def minimum_length(inp):    
    last_len = 0

    while last_len != len(inp):
        last_len = len(inp)
        inp = reduce_polymer(inp)
        
    return len(inp)

print minimum_length([x for x in inp])

units = set([x for x in inp if x >= 65])
minimum = 500000000000
for u in units:

    l = minimum_length([x for x in inp if x not in (u, u-32)])
    if l < minimum:
        minimum = l
    
print minimum

