sample = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

def run(stmnts):
    regs = {}
    maxval = 0
    maxval_end = 0
    for st in stmnts:
        p = st.split(" ")
        reg = p[0]
        op = p[1]
        val = int(p[2])
        cmpreg = p[4]
        cmpop = p[5]
        cmpval = int(p[6])

        if cmpreg not in regs:
            regs[cmpreg] = 0
        if reg not in regs:
            regs[reg] = 0
        doit = False
        if cmpop == ">":
            if regs[cmpreg] > cmpval:
                doit = True
        elif cmpop == ">=":
            if regs[cmpreg] >= cmpval:
                doit = True
        elif cmpop == "<":
            if regs[cmpreg] < cmpval:
                doit = True
        elif cmpop == "<=":
            if regs[cmpreg] <= cmpval:
                doit = True
        elif cmpop == "==":
            if regs[cmpreg] == cmpval:
                doit = True
        elif cmpop == "!=":
            if regs[cmpreg] != cmpval:
                doit = True
        if doit:
            if op == "inc":
                regs[reg] += val
                if regs[reg] > maxval:
                    maxval = regs[reg]
            elif op == "dec":
                regs[reg] -= val
                if regs[reg] > maxval:
                    maxval = regs[reg]

    for r in regs:
        if regs[r] > maxval_end:
            maxval_end = regs[r]
    
    return maxval_end, maxval, regs

print(run(sample.split("\n")))
print(run(open("input.txt", "r").readlines()))
   
   
   
   
