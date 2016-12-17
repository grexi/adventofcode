def invert(seq):
    s = []
    for c in seq:
        if c == '0':
            s.append('1')
        else:
            s.append('0')
    return "".join(reversed(s))

def dragon(seq, length):
    while len(seq) < length:
        
        seq = seq + "0" + invert(seq)
    return seq[:length]

def checksum(seq):
    csum = []
    while True:
        for i in range(0, len(seq),2):
            #print seq[i:i+2]
            if seq[i:i+2] in ("11", "00"):
                csum.append("1")
            else:
                csum.append("0")
        #print("Round %r" % (csum))
        if len(csum) % 2 == 0:
            seq = "".join(csum)
            csum = []
        else:
            break
    return "".join(csum)

print(checksum(dragon("10000", 20)))

print(checksum(dragon("01111010110010011", 35651584)))

