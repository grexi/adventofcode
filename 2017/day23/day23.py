
def get_val(x, regs):
	try:
		x_i = int(x)
		return x_i
	except:
		if x not in regs:
			regs[x] = 0
		return regs.get(x)

def execute(lines):
	regs = {}
	pgc = 0
	mulcount = 0
	while pgc >= 0 and pgc < len(lines):
		l = lines[pgc].strip()

		p = l.split(" ")

		if p[0] == "set":
			regs[p[1]] = get_val(p[2], regs)
			pgc += 1
		elif p[0] == "sub":
			regs[p[1]] = get_val(p[1], regs) - get_val(p[2], regs)
			pgc += 1
		elif p[0] == "mul":
			regs[p[1]] = get_val(p[1], regs) * get_val(p[2], regs)
			pgc += 1
			mulcount += 1
		elif p[0] == "jnz":
			x = get_val(p[1], regs)
			if x != 0:
				off = get_val(p[2], regs)
				pgc += off
			else:
				pgc += 1
	return mulcount

def execute2():
	b = 99
	c = b
	b *= 100
	b += 100000
	c = b
	c += 17000
	h = 0
	while b <= c:
		f = 1
		d = 2
		while d < b:        
		    if b % d == 0:
		        f = 0
		    d += 1

		if f == 0:
		    h += 1
		b += 17

	return h

		    

l = open("input.txt", "r").readlines()
print(execute(l))
print(execute2())

