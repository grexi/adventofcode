
def blocks(seq):
	pos = [0,0]
	dirs = [(0,1), (1,0), (0,-1), (-1,0)]
	dirIndex = 0

	steps = seq.split(",")
	for s in steps:
		s = s.strip()
		steps = int(s[1:])
		if s[0] == "R":
			dirIndex += 1
		else:
			dirIndex -= 1
		dirIndex = dirIndex % 4
		for c in range(steps):
			pos[0] += dirs[dirIndex][0]
			pos[1] += dirs[dirIndex][1]
	return abs(pos[0])+abs(pos[1])


def blocks2(seq):
	visited = {}
	pos = [0,0]
	dirs = [(0,1), (1,0), (0,-1), (-1,0)]
	dirIndex = 0

	steps = seq.split(",")
	for s in steps:
		s = s.strip()
		steps = int(s[1:])
		if s[0] == "R":
			dirIndex += 1
		else:
			dirIndex -= 1
		dirIndex = dirIndex % 4
		for c in range(steps):
			pos[0] += dirs[dirIndex][0]
			pos[1] += dirs[dirIndex][1]
			posS = "%s/%s" % (pos[0], pos[1])
			#print "Visiting %s" % posS
			if visited.has_key(posS):
				#print "Was already here! %s" % posS
				return abs(pos[0])+abs(pos[1])
			visited[posS] = 1
	return 0

if __name__ == "__main__":

	print blocks("R2, L3")
	print blocks("R2, R2, R2")
	print blocks("R5, L5, R5, R3")
	print blocks("R8, R4, R4, R8")


	print blocks("R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3")

	print blocks2("R2, L3")
	print blocks2("R2, R2, R2")
	print blocks2("R5, L5, R5, R3")
	print blocks2("R8, R4, R4, R8")

