sample = """0: 3
1: 2
4: 4
6: 4"""


def build_firewall(lines):
    fw = {}
    for l in lines:
        p = l.split(":")
        fw[int(p[0])] = [0, int(p[1].strip()), 1]
    #print(fw)
    return fw

def move_scanners(fw, delay=1):
    for s in fw:
        for _ in range((delay % (fw[s][1] + fw[s][1] - 2))):
            #print("shifting")
            fw[s][0] = (fw[s][0] + fw[s][2])
            if fw[s][0] == (fw[s][1] - 1):
                fw[s][2] = -1
            if fw[s][0] == 0:
                fw[s][2] = 1
    return fw

def calculate_penalty(fw, delay = 0):

    penalty = 0
    maxdepth = max(fw.keys())


    fw = move_scanners(fw, delay)

    for step in range(maxdepth+1):
        
        if step in fw:
            if fw[step][0] == 0:
                #print("Hit at %r %r" % (step, fw[step]))
                penalty += step * fw[step][1]
                if delay > 0:
                    return True
        fw = move_scanners(fw)
        if delay > 0 and penalty > 0:
            return True

    return penalty

print("penality of sample %r" % (calculate_penalty(build_firewall(sample.split("\n")))))
print("penality of sample %r" % (calculate_penalty(build_firewall(sample.split("\n")), 10)))
print("penality of sample %r" % (calculate_penalty(build_firewall(open("input.txt", "r").readlines()))))



delay = 33600

fw = build_firewall(open("input.txt", "r").readlines())

#print("Penality of sample %r" % (calculate_penalty(fw, 33600)))

while True:
    if calculate_penalty(fw, delay) == 0:
        print("found delay %r" % (delay))
        break
    for k in fw:
        fw[k][0] = 0
        fw[k][2] = 1
    delay += 1
    if (delay % 1000) == 0:
        print delay
            
