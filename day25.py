
def invert(ins):
    print("inverting %r" % ins)
    if len(ins) == 2:
        if ins[0] == "inc":
            ins[0] = "dec"
        else:
            ins[0] = "inc"
    elif len(ins) == 3:
        if ins[0] == "jnz":
            ins[0] = "cpy"
        else:
            ins[0] = "jnz"
    return ins

def execute(instructions, ipr, regs, mLen):
    outL = []

    while ipr < len(instructions) and len(outL) < mLen:

        parts = instructions[ipr]
        #print(parts)
        if parts[0] == "cpy":
            ipr += 1
            if parts[2] in "abcd":
                if parts[1] in "abcd":
                    regs[parts[2]] = regs[parts[1]]
                else:
                    regs[parts[2]] = int(parts[1])
        elif parts[0] == "inc":

            if parts[1] in "abcd":

                # Peephole optimize inc/dec/jnz loops

                # 4 cpy b c
                # 5 inc a          <<<< 0
                # 6 dec c          <<<< +1
                # 7 jnz c -2       <<<< +2
                # 8 dec d          <<<< +3
                # 9 jnz d -5       <<<< +4

                if ipr + 3 < len(instructions) and ipr - 1 >= 0 and instructions[ipr-1][0] == "cpy" and \
                    instructions[ipr+1][0] == "dec" and instructions[ipr+2][0] == "jnz" and \
                    instructions[ipr+3][0] == "dec" and instructions[ipr+4][0] == "jnz":

                    incop = parts[1]

                    cpysrc, cpydest = instructions[ipr-1][1:]
                    dec1op = instructions[ipr+1][1]
                    jnz1cond, jnz1off = instructions[ipr+2][1:]
                    dec2op = instructions[ipr+3][1]
                    jnz2cond, jnz2off = instructions[ipr+4][1:]

                    if cpydest == dec1op and dec1op == jnz1cond and \
                        dec2op == jnz2cond and \
                        jnz1off == "-2" and jnz2off == "-5":
                            # inner loop:
                            # incop += cpysrc
                            # dec1op <- 0

                            # outer loop:
                            # dec2op times

                            # net result:  incop += (cpysrc * dec2op)
                            # dec1op, dec2op <- 0
                            if cpysrc in "abcd":
                                cpysrc_v = regs[cpysrc]
                            else:
                                cpysrc_v = int(cpysrc)

                            if dec2op in "abcd":
                                dec2op_v = regs[dec2op]
                            else:
                                dec2op_v = int(dec2op)

                            regs[incop] += (cpysrc_v * dec2op_v)
                            regs[dec1op] = 0
                            regs[dec2op] = 0
                            ipr += 5
                            continue

                regs[parts[1]] += 1

            ipr += 1
        elif parts[0] == "dec":
            ipr += 1
            regs[parts[1]] -= 1
        elif parts[0] == "jnz":
            try:
                if parts[2] in "abcd":
                    step = regs[parts[2]]
                else:
                    step = int(parts[2])
                if parts[1] in "abcd":
                    if regs[parts[1]] != 0:
                        ipr += step
                    else:
                        ipr += 1
                else:
                    if int(parts[1]) != 0:
                        ipr += step
                    else:
                        ipr += 1
            except:
                ipr += 1

        elif parts[0] == "tgl":
            target = ipr
            if parts[1] in "abcd":
                target += regs[parts[1]]
            else:
                target += int(parts[1])
            if target >= 0 and target < len(instructions):
                instructions[target] = invert(instructions[target])
            ipr += 1
        elif parts[0] == "out":
            if parts[1] in "abcd":
                #print(regs[parts[1]])
                outL.append(regs[parts[1]])
            ipr += 1


    return outL


instructions = open("day25/input.txt", "r").readlines()
#instructions = """cpy 2 a
#tgl a
#tgl a
#tgl a
#cpy 1 a
#dec a
#dec a""".split("\n")
instructions = [ i.strip().split() for i in instructions ]
ipr = 0
for i in range(188, 191):
    #print("Checking %r" % i)
    regs = {"a":i , "b": 0, "c": 0, "d": 0 }
    outL = execute(instructions, ipr, regs, 100)
    error = False
    for j in range(len(outL)):
        if outL[j] % 2 != j % 2:
            #print("outL %r %r %r %r" % (outL[j], outL[j] %2, j, j%2))
            error = True
            continue
    if not error:
        print("What about %r" % i)
print("%r" % regs)
