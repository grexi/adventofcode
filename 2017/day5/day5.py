

def steps(pgm):
	stc = 0
	i = 0
	l = len(pgm)
	while i >= 0 and i < l:
		jmp = pgm[i]
		pgm[i] += 1
		i += jmp
		stc += 1
	return stc

def steps2(pgm):
	stc = 0
	i = 0
	l = len(pgm)
	while i >= 0 and i < l:
		jmp = pgm[i]
		if jmp >= 3:
			pgm[i] -= 1
		else:
			pgm[i] += 1
		i += jmp
		stc += 1
	return stc



s = [int(x.strip()) for x in open("input.txt", "r").readlines()]
print("steps %r" % (steps([0, 3, 0, 1, -3])))
print("steps %r" % (steps(s)))

s = [int(x.strip()) for x in open("input.txt", "r").readlines()]
print("steps2 %r" % (steps2([0, 3, 0, 1, -3])))
print("steps2 %r" % (steps2(s)))
