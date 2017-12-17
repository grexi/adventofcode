def spinlock(jump, length=2017):
    l = [0]
    idx = -1
    for i in xrange(1, length+1):
        idx = (idx + jump) % (i)
        l.insert(idx + 1, i)
        idx = (idx + 1) % (i+1)
    return l

def spinlock2(jump, length=50000000):

    idx = -1
    afterzero = -1
    for i in xrange(1, length+1):
        idx = (idx + jump) % (i)
        if idx == 0:
            afterzero = i
        idx = (idx + 1) % (i+1)
    return afterzero


l2 = spinlock(345)
print(l2[l2.index(2017)+1])

print(spinlock2(345))
