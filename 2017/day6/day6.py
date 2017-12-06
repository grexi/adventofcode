def redistribute(blocks):
	states = {}
	blocklen = len(blocks)

	cnt = 0
	while "".join(("%s" % b for b in blocks)) not in states:
		
		states["".join(("%s" % b for b in blocks))] = cnt
		#print("Starting at %r" % blocks)
		maximum = max(blocks)
		maxindex = blocks.index(maximum)
		blocks[maxindex] = 0
		maxindex += 1
		while maximum > 0:
			blocks[maxindex%blocklen] += 1
			#print("Shifted to at %r" % blocks)
			maximum -= 1
			maxindex += 1
		cnt += 1

	return len(states), (cnt- states["".join(("%s" % b for b in blocks))])


print(redistribute([0,2,7,0]))

print(redistribute([int(x) for x in open("input.txt", "r").read().strip().split("\t")]))
