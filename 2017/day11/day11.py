

def hexsteps(instr):
    steps = instr.strip().split(",")
    count = {"nw": 0, "n": 0, "ne": 0, "s": 0, "se": 0, "sw": 0}
    for s in steps:
        if s in count:
            count[s] += 1

    #print "total counts %r" % count
    if count["nw"] > count["se"]:
        count["nw"] -= count["se"]
        count["se"] = 0
    else:
        count["se"] -= count["nw"]
        count["nw"] = 0
    if count["n"] > count["s"]:
        count["n"] -= count["s"]
        count["s"] = 0
    else:
        count["s"] -= count["n"]
        count["n"] = 0

    if count["ne"] > count["sw"]:
        count["ne"] -= count["sw"]
        count["sw"] = 0
    else:
        count["sw"] -= count["ne"]
        count["ne"] = 0

    min_ne_s = min(count["ne"], count["s"])
    count["ne"] -= min_ne_s
    count["s"] -= min_ne_s
    count["se"] += min_ne_s
    
    min_nw_s = min(count["nw"], count["s"])
    count["nw"] -= min_nw_s
    count["s"] -= min_nw_s
    count["sw"] += min_nw_s

    min_se_n = min(count["se"], count["n"])
    count["se"] -= min_se_n
    count["n"] -= min_se_n
    count["ne"] += min_se_n
    
    min_sw_n = min(count["sw"], count["n"])
    count["sw"] -= min_sw_n
    count["n"] -= min_sw_n
    count["nw"] += min_sw_n

    min_se_sw = min(count["se"], count["sw"])
    count["sw"] -= min_se_sw
    count["se"] -= min_se_sw
    count["s"] += min_se_sw

    min_ne_nw = min(count["ne"], count["nw"])
    count["nw"] -= min_ne_nw
    count["ne"] -= min_ne_nw
    count["n"] += min_ne_nw

    #print "reduced counts %r" % count

    sumc = 0
    for c in count:
        sumc += count[c]
    return sumc, count

print(hexsteps("ne,ne,ne"))
print(hexsteps("ne,ne,s,s"))
print(hexsteps("se,sw,se,sw,sw"))


inputstr = open("input.txt", "r").read()
print(hexsteps(inputstr))

maxsteps = 0
maxcount = 0
for i in range(len(inputstr)):

    s, countc = hexsteps(inputstr[:i])
    print("s = %s" % (s))
    if s > maxsteps:
        maxsteps = s
        maxcount = countc

print("maximum: %s" % maxsteps )
print("maximum %s" % maxcount)


