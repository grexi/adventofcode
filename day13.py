import sys


def build_maze(n, secret):
	maze = []
	for y in range(n):
		r = []
		for x in range(n):
			sums = x*x + 3*x + 2*x*y + y + y*y + secret
			if bin(sums).count("1") % 2 == 0:
				r.append(".")
			else:
				r.append("#")
		maze.append(r)
	return maze


def print_maze(m):
	for r in m:
		print "".join(r)

visited = {}
visited_2 = {}
min_solution = 100000000000000000000
steps = 0
def find_path(m, pos, target, depth=0):
	global visited, visited_2, min_solution, steps

	print("Step %r %r %s" % (pos, depth, target))

	
	posS = "%sx%s" % (pos[0], pos[1])
	if posS in visited and depth >= visited[posS]:
		print("visited")
		return False
	visited[posS] = depth

	if pos[0] < 0 or pos[1] < 0:

		print ("negative")
		return False
	if pos[0] >= len(m) or pos[1] >= len(m[0]):
		print ("outside of maze")
		return False
	if m[pos[0]][pos[1]] == '#':
		print ("wall")
		return False

	if depth <= 50:
		visited_2[posS] = depth
	if pos[0] == target[0] and pos[1] == target[1]:
		print ("Target")
		return True
	directions = [ (0,1), (1,0), (-1, 0), (0, -1)]
	for d in directions:
		npos = [pos[0] + d[0], pos[1] + d[1]]
		if find_path(m, npos, target, depth+1):
			
			print("solution after %s steps" % (depth+1))
			if (depth+1) < min_solution:
				min_solution = depth+1

test = False
if test == True:
	m = build_maze(10, 10)
	print_maze(m)

	find_path(m, [1,1], [4,7])
	print ("Min solution: %r" % min_solution)
if test == False:

	m = build_maze(50, 1364)
	print_maze(m)

	find_path(m, [1,1], [39,31])
	print ("Min solution: %r" % min_solution)

	print ("Locations: %r" % (len(visited_2)))

			
