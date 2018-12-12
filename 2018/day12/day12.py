inp = open("input.txt", "r")

start = inp.readline().split(":")[1].strip()
pots = ["." for _ in xrange(10000)]
for i in xrange(len(start)):
    pots[i] = start[i]

inp.readline()
rules = {}
for r in inp.readlines():
    parts = [s.strip() for s in r.split("=>")]
    rules[tuple(x for x in parts[0])] = parts[1]

#print start
#print rules
#print pots


def potsum(pots):
    s = 0
    h = len(pots)/2
    for i in xrange(-h, h):
        if pots[i] == '#':
            s += i
    return s

def get_part(pots, x):
    if -3 <= x <= 1 :
        sub = pots[-(2-x):] + pots[:x+3]
    else:
        sub = pots[x-2:x+3]
    
    ssub = tuple(sub)
    return ssub

h = len(pots)/2
total = 2100
res = []
for i in xrange(total):
    #print "".join(pots)    
    npots = pots[:]
    for x in xrange(-h, h):
        ssub = get_part(pots, x)    
        #print "Pot %r %r" % (x, ssub)
        if ssub in rules:
            npots[x] = rules[ssub]
        else:
            npots[x] = '.'
    pots = npots
    
    if i == (20-1):
        print ("20. Generation %r " % potsum(pots))
    if i> 0 and i % 1000 == 0:
        res.append([i, potsum(pots)])
    

#print potsum(pots)
print res
k = (res[1][1] - res[0][1]) / (res[1][0] - res[0][0])
d = res[1][1] - k*res[1][0]
print "linear y = %d*x + %d" % (k, d)
print "50000000000. Generation = %d" % (k*(50000000000-1) + d)