import collections

def distances(maze):
	pos = None
	for x in range(len(maze)):

		for y in range(len(maze[0])):
			if maze[x][y] == "0":
				pos = (x, y)
				break
	if not pos:
		return False

	visits = {}
	distances = {}
	curLoc = "0"
	# up, left, down, right
	dirs = [(1,0), (0, -1), (-1, 0), (0, 1)]
	q = collections.deque()
	steps = 0
	while True:
		for i in range(4):	
			newx = pos[0]+dirs[i][0]
			newy = pos[1]+dirs[i][1]
			vstr = "%sx%sx%s" % (curLoc, newx, newy)
			if newx < 0 or newx >= len(maze):
				continue
			if newy < 0 or newy >= len(maze[0]):
				continue
			if vstr in visits:
				continue
			visits[vstr] = 1
			if maze[newx][newy] == '#':
				continue
			
			if maze[newx][newy] == '.':
				q.append( ( (newx,newy), curLoc, steps+1) )
			else:
				if maze[newx][newy] == curLoc:
					continue

				if curLoc not in distances:
					distances[curLoc] = {}		
				if maze[newx][newy] not in distances[curLoc]:
					distances[curLoc][maze[newx][newy]] = steps+1
					q.append( ( (newx,newy), curLoc, steps+1) )
					q.append( ( (newx,newy), maze[newx][newy], 0) )
		if len(q) == 0:
			break
		(pos, curLoc, steps) = q.popleft()
	print("distances %r" % distances)
	return distances

def path(distances, start, total):
	q = collections.deque()
	steps = 0
	visits = ["0"]
	minpath = 100000000000000000
	minpath2 = 100000000000000000
	pvisits = {}
	i = 0
	while i<1000000:
		if len(set(visits)) == total:# and visits[-1] == "0":
			#print("____solution: %5d %r" % (steps, visits))
			if visits[-1] == "0" and steps < minpath2:
				print("----new solution: %5d %r" % (steps, visits))
				minpath2 = steps
				i = 0			
			if steps < minpath:
				print("####new solution: %5d %r" % (steps, visits))
				minpath = steps
				i = 0			


		for t in distances[start]:
			vstr = "%r%r%r" % (visits, t, steps)
			if vstr in pvisits:
				continue
			pvisits[vstr] = 1
			if t == "0" and len(set(visits)) != total:

				continue
			else:
				if t == "0":
					#print("Searching for 0!! %r" % (visits))


					#print("Appending %r" % ((visits + [t], t, steps + distances[start][t]),) )
					pass
			q.append( (visits + [t], t, steps + distances[start][t]))
		if len(q) == 0:
			break
		(visits, start, steps) = q.popleft()
		i+=1
	return minpath, minpath2
			
if False:
	inmaze = """###########
	#0.1.....2#
	#.#######.#
	#4.......3#
	###########"""

	dis1 = distances(inmaze.split("\n"))

	print(dis1)
	p = path(dis1, "0", 5)
	print(p)
if True:
	inmaze2 = open("day24/input.txt", "r").readlines()
	dist = distances(inmaze2)
	print(dist)
	print("Now searching path")
	p = path(dist, "0", 8)
	print(p)

