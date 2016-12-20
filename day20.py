def ipblock(seq):

	blocks = []
	for block in seq:
		block = map(int, block.strip().split("-"))
		blocks.append(block)	

	blocks.sort()
	oldlen = len(blocks)

	newblocks = []
	it = 0
	while len(newblocks) != oldlen:
		
		#print("Iteration %r" % it)
		#print("Blocks %r" % (blocks))
		it += 1

		newblocks = []
		merged = set()
		oldlen = len(blocks)
		for i in range(oldlen):
			l = blocks[i]
			if i in merged:
				continue
			found = False
			for j in range(oldlen):
				if i != j:
					r = blocks[j]
					if j in merged:
						continue
					#merge blocks
	
					if (l[1] >= r[0] and l[1] <= r[1]) or \
					   (r[1] >= l[0] and r[1] <= l[1]) or \
						(l[1]+1 == r[0]):
						#print("Blocks %r %r can be merged to %r" % (l,r, [min(l[0], r[0]), max(l[1], r[1])]))
						newblocks.append([ min(l[0], r[0]), max(l[1], r[1]) ])
						merged.add(i)
						merged.add(j)
						found = True
						break
			if found == False:
				newblocks.append(l)
				merged.add(i)

		#print("Newblocks %r" % newblocks)
		blocks = newblocks
		#blocks.sort()
	newblocks.sort()


	allowed = 0
	for i in range(0, len(newblocks)-1):
		l = newblocks[i]
		r = newblocks[i+1]
		#print("Range from %r to %r is allowed" % (l, r))
		#print("Range from %r to %r is allowed %r" % (l[1], r[0], ((r[0] - l[1] - 1 ))))
		allowed += (r[0] - l[1] - 1 )	
		
	return newblocks[0][1]+1, allowed


f = open("day20/input.txt", "r")
print(ipblock(f.readlines()))

