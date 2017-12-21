
def break_pattern(pattern):
	return [[y for y in x] for x in pattern.split("/")]

def join_pattern(p):
	return "/".join(("".join(x) for x in p))

def rotate(pattern, count):
	p = break_pattern(pattern)
	for i in xrange(count):
		p = zip(*p[::-1])
	return join_pattern(p)

def flip(pattern):
	p = break_pattern(pattern)
	return "/".join(("".join(reversed(x)) for x in p))

def parse_rules(lines):
	rules = {}
	for l in lines:
		p = l.split("=>")
		result = p[1].strip()
		inp = p[0].strip()
		
		rules[inp] = result
		rules[rotate(inp, 1)] = result
		rules[rotate(inp, 2)] = result
		rules[rotate(inp, 3)] = result
		flinp = flip(inp)
		rules[flinp] = result
		rules[rotate(flinp, 1)] = result
		rules[rotate(flinp, 2)] = result
		rules[rotate(flinp, 3)] = result

	return rules

def apply_pattern(pattern, rules):
	p = break_pattern(pattern)

	dim = len(p)
	if dim % 2 == 0:
		rep = 2
		def scale(v):
			return (v/2)*3
	elif dim % 3 == 0:
		rep = 3
		def scale(v):
			return (v/3)*4
	else:
		#print("DIM is %r" % (dim))
		return 
	res = [[0 for i in xrange(scale(dim))] for j in xrange(scale(dim))]
	#print(res)
	for i in xrange(0, dim, rep):
		for j in xrange(0, dim, rep):
			subp = [x[j:j+rep] for x in p[i:i+rep]]
			subp = join_pattern(subp)
			new = rules.get(subp)
			#print("%s Replacing %r with %r %r %r" % (rep, subp, new,i, j))			
			newp = break_pattern(new)
			newdim = len(newp)

			for g in xrange(newdim):

				for h in xrange(newdim):
					#print("setting %r %r %r [%r %r] %r" % (res, i, j, scale(i)+g, scale(j)+h, newp[g][h]))
					res[scale(i)+g][scale(j)+h] = newp[g][h]


	return "/".join(("".join(x) for x in res))

sample="""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""
rules_sample = parse_rules(sample.split("\n"))


rules = parse_rules(open("input.txt", "r").readlines())


cur_pattern = ".#./..#/###"

cur_pattern = apply_pattern(cur_pattern, rules_sample)
cur_pattern = apply_pattern(cur_pattern, rules_sample)
print(cur_pattern.count("#"))

cur_pattern = ".#./..#/###"
for i in range(5):
	cur_pattern = apply_pattern(cur_pattern, rules)

print(cur_pattern.count("#"))
cur_pattern = ".#./..#/###"
for i in range(18):
	cur_pattern = apply_pattern(cur_pattern, rules)

print(cur_pattern.count("#"))
