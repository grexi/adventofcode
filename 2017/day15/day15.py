
import Queue
def judge(starta, startb):
    gena = starta
    genb = startb
    match = 0
    for i in range(40000000):
        gena = gena*16807 % 2147483647
        genb = genb*48271 % 2147483647
        if gena & 0xffff == genb & 0xffff:
            match += 1
    return match

def judge2(starta, startb):
    gena = starta
    genb = startb
    res_a = Queue.Queue()
    res_b = Queue.Queue()
    match = 0
    comp = 5000000
    while comp > 0:
        #if comp % 1000000 == 0:
        #    print(comp)
        gena = gena*16807 % 2147483647
        genb = genb*48271 % 2147483647
        if gena % 4 == 0:
            res_a.put(gena)
        if genb % 8 == 0:
            res_b.put(genb)
        if not res_a.empty() and not res_b.empty():
            a = res_a.get()
            b = res_b.get()
            if a & 0xffff == b & 0xffff:
                match +=1
            comp -= 1
    return match

        

#print(judge(65,8921))
#print(judge2(65,8921))
print(judge(618,814))
print(judge2(618,814))
