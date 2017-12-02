

def min_max_sum(line):
	v = [int(x) for x in line.split("\t")]
	return max(v), min(v)

def modulo_sum(line):
	v = [int(x) for x in line.split("\t")]
	l = len(v)
	for i in range(l):
		for j in range(l):
			if i == j:
				continue
			if (v[i] % v[j]) == 0:
				return (v[i],v[j])

lines = open("input.txt", "r").readlines()
sum_minmax = 0
sum_modulo = 0

for l in lines:
	mx, mi = min_max_sum(l)
	
	sum_minmax += mx - mi
	a,b = modulo_sum(l)
	sum_modulo += (max(a,b) / min(a,b))

print("Part 1 %d" % (sum_minmax))
print("Part 2 %d" % (sum_modulo))


