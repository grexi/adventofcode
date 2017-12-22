def infect_map(lines):
	maxsize = 5000
	m = [["." for _ in xrange(maxsize)] for _ in xrange(maxsize)]
	dim = len(lines)
	starti = maxsize/2 - dim/2
	startj = maxsize/2 - dim/2
	for i in xrange(dim):
		for j in xrange(dim):
			m[i+starti][j+startj] = lines[i][j]

	pos = [maxsize/2, maxsize/2 ]
	curdir = 0
	dirs = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
	infcount = 0
	for i in xrange(10000):
		if m[pos[0]][pos[1]] == '#':
			curdir = (curdir + 1) % 4
			m[pos[0]][pos[1]] = '.'
		else:
			curdir = (curdir - 1) % 4
			m[pos[0]][pos[1]] = '#'
			infcount += 1
		pos[0] += dirs[curdir][0]
		pos[1] += dirs[curdir][1]
		
		#print("\n".join( ("".join(l) for l in m) ))
	print(infcount)

def infect_map2(lines):
	maxsize = 5000
	m = [["." for _ in xrange(maxsize)] for _ in xrange(maxsize)]
	dim = len(lines)
	starti = maxsize/2 - dim/2
	startj = maxsize/2 - dim/2
	for i in xrange(dim):
		for j in xrange(dim):
			m[i+starti][j+startj] = lines[i][j]

	pos = [maxsize/2, maxsize/2 ]
	curdir = 0
	dirs = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
	infcount = 0
	for i in xrange(10000000):
		if m[pos[0]][pos[1]] == '#':
			curdir = (curdir + 1) % 4
			m[pos[0]][pos[1]] = 'F'
		elif m[pos[0]][pos[1]] == 'W':
			m[pos[0]][pos[1]] = '#'
			infcount += 1
		elif m[pos[0]][pos[1]] == '.':
			curdir = (curdir - 1) % 4
			m[pos[0]][pos[1]] = 'W'
		elif m[pos[0]][pos[1]] == 'F':
			curdir = (curdir + 2) % 4
			m[pos[0]][pos[1]] = '.'

		pos[0] += dirs[curdir][0]
		pos[1] += dirs[curdir][1]
		
		#print("\n".join( ("".join(l) for l in m) ))
	print(infcount)

sample = """..#
#..
..."""
infect_map(sample.split("\n"))

infect_map(open("input.txt", "r").readlines())


infect_map2(sample.split("\n"))

infect_map2(open("input.txt", "r").readlines())

