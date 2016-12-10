bots = {}
outputs = {}

def add_value(bots, outputs, botNr, val):
    if botNr not in bots:
        bots[botNr] = { "val": [], "cmd": [] }
    bots[botNr]["val"].append(val)
    if len(bots[botNr]["val"]) == 2:
        process_bot(bots, outputs, botNr)    

def add_command(bots, outputs, botNr, target1, targetNr1, target2, targetNr2):
    if botNr not in bots:
        bots[botNr] = { "val": [], "cmd": [] }
    bots[botNr]["cmd"].append( [target1, targetNr1])
    bots[botNr]["cmd"].append( [target2, targetNr2])
    if len(bots[botNr]["val"]) == 2:
        process_bot(bots, outputs, botNr)  
    
def bot(bots, outputs,  seq):
    parts = seq.split()
    if parts[0] == "value":
        value = int(parts[1])
        botNr = int(parts[5])
        add_value(bots, outputs, botNr, value)


    elif parts[0] == "bot":
        botNr = int(parts[1])
        target1 = parts[5]
        targetNr1 = int(parts[6])
        target2 = parts[10]
        targetNr2 = int(parts[11])
        add_command(bots, outputs, botNr, target1, targetNr1, target2, targetNr2)

def process_bot(bots, outputs,  botNr):

    bot = bots[botNr]
    #print("Processing bot %r %r" % (botNr, bot))
    low, high = sorted(bot["val"])
    if low == 17 and high == 61:
        print("It's bot nr %r" % botNr)
    if len(bots[botNr]["cmd"]) < 2:
        return

    cmd = bots[botNr]["cmd"][0]
    if cmd[0] == "output":
        outputs[cmd[1]] = low
    elif cmd[0] == "bot":
        add_value(bots, outputs, cmd[1], low)

    cmd = bots[botNr]["cmd"][1]
    if cmd[0] == "output":
        outputs[cmd[1]] = high
    elif cmd[0] == "bot":
        add_value(bots, outputs, cmd[1], high)
    bots[botNr]["val"] = []
    bots[botNr]["cmd"] = []
        

r = open("day10/input.txt", "r")

for line in r.readlines():
    #print(line)
    bot(bots, outputs, line)

    
print outputs[0] * outputs[1] * outputs[2]
    #print("%r %r" % (bots, outputs))
