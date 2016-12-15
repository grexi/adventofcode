import time

def bruteForce(discs, starts):
    t = 1
    l = len(discs)
    while True:
        match = 0
        for i in range(l):
            if ((starts[i]+i+1+t) % discs[i]) == 0:
                match += 1
        if match == l:
            return t
        t+=1

def ext_gcd(a, b):
    u, s, v, t = 1, 0, 0, 1
    while b != 0:
        q = a//b
        u, s, v, t = s, u-q*s, t, v-q*t
        a, b = b, a % b
    return a, u, v

def inverse(a,b):
    (c, x, y) = ext_gcd(a, b)
    return x

def chinese_rem(nn, rr):
    if len(nn)==1:
        return nn[0], rr[0]
    else:
        j=len(nn)//2
        m, a=chinese_rem(nn[:j], rr[:j])
        n, b=chinese_rem(nn[j:], rr[j:])
        u=inverse(m, n)
        x=u*(b-a)%n*m+a
    return m*n, x

           
def intelligent(discs, starts):
    zeromod = []
    # Find resulting "a" for each disc:
    # x === a_n mod m_n
    # where as a_n = ( neg pos at 0) mod m_n
    for i in range(len(starts)):
        zeromod.append((-starts[i]-(i+1)) % discs[i])
    return chinese_rem(discs, zeromod)[1]

test = False
if test:
    print(bruteForce([5,2], [4, 1]))
    print(intelligent([5,2], [4, 1]))
else:
    """
    Disc #1 has 5 positions; at time=0, it is at position 2.
    Disc #2 has 13 positions; at time=0, it is at position 7.
    Disc #3 has 17 positions; at time=0, it is at position 10.
    Disc #4 has 3 positions; at time=0, it is at position 2.
    Disc #5 has 19 positions; at time=0, it is at position 9.
    Disc #6 has 7 positions; at time=0, it is at position 0.
    """
    times = []
    start = time.time()
    print(bruteForce([5,13,17,3,19,7], [2,7,10,2,9,0]))
    end = time.time()
    print("Took %.2f s" % (end-start))
    start = time.time()
    print(bruteForce([5,13,17,3,19,7,11], [2,7,10,2,9,0,0]))
    end = time.time()
    print("Took %.2f s" % (end-start))
    start = time.time()
    print(intelligent([5,13,17,3,19,7], [2,7,10,2,9,0]))
    end = time.time()
    print("Took %.2f s" % (end-start))
    start = time.time()
    print(intelligent([5,13,17,3,19,7,11], [2,7,10,2,9,0,0]))
    end = time.time()
    print("Took %.2f s" % (end-start))    

