

def cap_sum(v):
    sums = 0
    i = 0
    for i in range(len(v)-1):
        if v[i] == v[i+1]:
            sums += int(v[i])
    if v[0] == v[-1]:
        sums += int(v[0])
    return sums

def cap_sum_circle(v):
    sums = 0
    i = 0
    llen = len(v)
    loff = llen/2
    for i in range(llen):
        if v[i] == v[(i+loff)%llen]:
            sums += int(v[i])
    return sums

if True:
    print("Sum %s" %  (cap_sum("1122")))
    print("Sum %s" %  (cap_sum("1111")))
    print("Sum %s" %  (cap_sum("1234")))
    print("Sum %s" %  (cap_sum("91212129")))
    print("Sum %s" %  (cap_sum(open("input.txt", "r").read().strip())))

if True:
    print("Sum2 %s" %  (cap_sum_circle("1212")))
    print("Sum2 %s" %  (cap_sum_circle("1221")))
    print("Sum2 %s" %  (cap_sum_circle("123425")))
    print("Sum2 %s" %  (cap_sum_circle("123123")))
    print("Sum2 %s" %  (cap_sum_circle("12131415")))
    print("Sum2 %s" %  (cap_sum_circle(open("input.txt", "r").read().strip())))
