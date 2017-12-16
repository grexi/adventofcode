def do_s(pgms, rot, l):
    pgms = pgms[(-rot):] + pgms[:(-rot)]    
    return pgms

def do_x(pgms, ind_a, ind_b):
    x = pgms[ind_b]
    pgms[ind_b] = pgms[ind_a]
    pgms[ind_a] = x
    return pgms

def do_p(pgms, a, b):
    ind_a = pgms.index(a)
    ind_b = pgms.index(b)
    return do_x(pgms, ind_a, ind_b)

def dance(steps, pgms, reps=1):
    steps = steps.split(",")
    pgms = [x for x in pgms]
    l = len(pgms)
    parsed_steps = []
    seen = []
    for s in steps:
        if s[0] == "s":
            rot = int(s[1:]) % l
            parsed_steps.append(("s", rot))
        elif s[0] == "x":
            p = s[1:].split("/")
            parsed_steps.append(("x", int(p[0]), int(p[1])))
        elif s[0] == "p":
            p = s[1:].split("/")
            parsed_steps.append(("p", p[0], p[1]))

    for i in xrange(reps):
        p = ''.join(pgms)
        if p in seen:
            return seen[reps % i]
        seen.append(p)
        for s in parsed_steps:

            if s[0] == "s":
                pgms = do_s(pgms, s[1], l)
            elif s[0] == "x":
                pgms = do_x(pgms, s[1], s[2])
            elif s[0] == "p":
                pgms = do_p(pgms, s[1], s[2])                 
    return "".join(pgms)

print(dance("""s1,x3/4,pe/b""", "abcde"))

print(dance(open("input.txt", "r").read().strip(), "abcdefghijklmnop"))
print(dance(open("input.txt", "r").read().strip(), "abcdefghijklmnop", 1000000000))
