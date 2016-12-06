import operator

freqs = []

def freq(seq):
	global freqs
	seq = seq.strip()
	if len(freqs) < len(seq):
		for s in seq:
			freqs.append({})
	i = 0
	for s in seq:
		if s not in freqs[i]:
			freqs[i][s] = 0
		freqs[i][s] += 1
		i+=1


r = open("day6/input.txt", "r")		

for line in r.readlines():
	freq(line)

for f in freqs:
	maximum = sorted(f.items(), key=operator.itemgetter(1))[0][0]
	#print "%r" % (maximum)
	print maximum,

