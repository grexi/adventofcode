import string


def parse_line(inseq):
    seq = []
    sp = inseq.split(" ")
    for s in sp:
        if s == '':
            continue
        seq.append(int(s))    
    return seq

def triangle(inseq):

    seq = parse_line(inseq)

    return is_triangle(seq)

def triangle2(seqs):
    sp = map(parse_line, seqs)
    
    t1 = [sp[0][0], sp[1][0], sp[2][0]]
    t2 = [sp[0][1], sp[1][1], sp[2][1]]
    t3 = [sp[0][2], sp[1][2], sp[2][2]]
    sums = 0
    if is_triangle(t1):
        sums +=1
    if is_triangle(t2):
        sums += 1
    if is_triangle(t3):
        sums += 1
    return sums


def is_triangle(seq):
    return ((seq[0] + seq[1]) > seq[2]) and ((seq[0] + seq[2]) > seq[1]) and ((seq[1] + seq[2]) > seq[0])
    


if __name__ == "__main__":
    infile = open("day3/input.txt")
    totaltriangle = 0
    curlines = []
    for line in infile.readlines():
        curlines.append(line)
        if len(curlines) == 3:
            totaltriangle += triangle2(curlines)
            curlines = []
#        if triangle(line):
#            totaltriangle += 1
    print("Total: %r" % totaltriangle)
