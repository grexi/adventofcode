

def execute(instructions, ipr, regs):
    while ipr < len(instructions):
        ins = instructions[ipr].strip()
        #print "executing %r" % ins
        #print "%r %r" % (ipr, regs)
        parts = ins.split()
        if parts[0] == "cpy":
            ipr += 1
            if parts[1] in "abcd":
                regs[parts[2]] = regs[parts[1]]
            else:
                regs[parts[2]] = int(parts[1])
        elif parts[0] == "inc":
            ipr += 1
            regs[parts[1]] += 1
        elif parts[0] == "dec":
            ipr += 1
            regs[parts[1]] -= 1
        elif parts[0] == "jnz":
            if parts[1] in "abcd":
                if regs[parts[1]] != 0:
                    ipr += int(parts[2])
                else:
                    ipr += 1
            else:
                if int(parts[1]) != 0:
                    ipr += int(parts[2])
                else:
                    ipr += 1




instructions = open("day12/input.txt", "r").readlines()

ipr = 0
regs = {"a":0 , "b": 0, "c": 1, "d": 0 }
execute(instructions, ipr, regs)
print("%r" % regs)
