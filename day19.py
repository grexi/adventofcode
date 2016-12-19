def winning_elve(nr):
    elves = [1 for i in range(nr)]
    while elves.count(0) < (nr-1):
        for i in range(nr):
            if elves[i] > 0:
                j = (i+1) % nr
                while elves[j] == 0:
                    j = (j+1) % nr
                    
                elves[i] += elves[j]
                elves[j] = 0

    for i in range(nr):
        if elves[i] != 0:
            return i+1

def winning_elve2(nr):
    elves = [i for i in range(1,nr+1)]
    i = 0
    curLen = nr
    while curLen > 1:
        if (curLen % 100) == 0:
            print("%r remaining" % curLen)
        #print("Looking at %r with %r" % (i, elves))
        toStealI = ((curLen // 2) + i) % curLen
        #toSteal = elves[toStealI]
        #print("Taking from %r " % toSteal)
        elves.pop(toStealI)
        
        curLen -= 1
        if toStealI < i:    
            i = i % curLen
        else:
            i = (i+1) % curLen
    return elves[0]        

def winning_elve3(nr):
    elves = [1 for i in range(nr)]
    curLen = nr
    i = 0
    cnt = 0
    while curLen > 1:
        cnt += 1
        if cnt % 1000 == 0:
            print("Remaining %r" % curLen)
        toStealI = (curLen // 2)
        i = i % nr

        while elves[i] == 0:
            i = (i+1) % nr
        #print("I'm at %r - steal is %r steps away" % (i, toStealI))
        j = (i+1) % nr
        while toStealI > 0:
            if elves[j] != 0:
                toStealI -= 1
            j = (j+1) % nr
            
        #print("Elve %r steals from %r" % (i+1, j+1))                    
        #elves[i] += elves[j]
        elves[j] = 0
        curLen -= 1
        i += 1

    for i in range(nr):
        if elves[i] != 0:
            return i+1

#print(winning_elve(5))
#print(winning_elve(3004953))

#print(winning_elve2(5))
#print(winning_elve2(3004953))
 
print(winning_elve3(5))
print(winning_elve3(3004953))
           
