import re
import copy
import json
import md5
from collections import deque

line = re.compile("/dev/grid/node-x(\d*)-y(\d*)\s*(\d*)T\s*(\d*)T\s*(\d*)T\s*(\d*)%")

def build_nodes(dflines):
	nodes = []
	for n in dflines:
		g = line.match(n).groups()
		node = {
			"x": int(g[0]), "y": int(g[1]),
			"size": int(g[2]), "used": int(g[3]),
			"avail": int(g[4]), "perc": int(g[5])
		}
		print("%r %r" % (n, node))
		nodes.append(node)
	return nodes
		
def generate_grid(nodes):
	grid = [[ 1 for x in range(31)] for y in range(32)]
	for n in nodes:
		grid[n["x"]][n["y"]] = n
	return grid


f = open("day22/input.txt", "r")
nodes = build_nodes(f.readlines()[2:])

pairs = []
for n_a in nodes:
	if n_a["used"] != 0:
		for n_b in nodes:
			if n_a == n_b:
				continue
			if n_a["used"] <= n_b["avail"]:
				#print("n_a %r would fit in n_b %r" % (n_a, n_b))
				pairs.append( [n_a, n_b] )

def print_grid(grid):
	for row in grid:
		for c in row:
			if c["used"] == 0:
				print("_"),
			else:
				print ("%s" % (c["perc"] > 90 and "#" or ".")),
		print

print(len(pairs))
grid = generate_grid(nodes)
print_grid(grid)


def find_possible_moves(grid):
	dirs = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
	moves = []
	for x in range(len(grid)):
		for y in range(len(grid[0])):

			for d in dirs:
				nx = x + d[0]
				ny = y + d[1]
				#print("checking grid %r %r to %r %r  = %r" % (x,y, nx, ny, grid[x][y]))
				if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[y]):
					#print("possible"),
					if grid[nx][ny]["avail"] >= grid[x][y]["used"] and \
						grid[x][y]["used"] > 0:
						#print("allowed"),
						moves.append( ((x,y), (nx,ny)) )

	return moves
				

def search_path(grid, end):
	print("Searching for path %r" % (end))
	queue = deque()
	visits = {}
	while not (grid[0][0]["x"] == end[0] and grid[0][0]["y"] == end[1]):
		sgrid = grid
		depth = 0		
		if len(queue) > 0:
			grid, m, depth = queue.popleft()
			#print("executing step %r %r" % (m))
			sgrid = copy.deepcopy(grid)
			sp = sgrid[m[0][0]][m[0][1]]["used"]
			sgrid[m[0][0]][m[0][1]]["used"] -= sp
			sgrid[m[0][0]][m[0][1]]["avail"] += sp
			sgrid[m[1][0]][m[1][1]]["used"] += sp
			sgrid[m[1][0]][m[1][1]]["avail"] -= sp
			#print_grid(grid)
			if (sgrid[0][0]["x"] == end[0] and sgrid[0][0]["y"] == end[1]):
				print("Found it - here! %r" % depth)
		digest = md5.md5(json.dumps(sgrid)).hexdigest()
		if digest not in visits:
			visits[digest] = 1
			moves = find_possible_moves(sgrid)
			#print("Find moves %r" % (moves))
			for m in moves:
				queue.append( (sgrid, m, depth+1) )



print(search_path(grid, [31, 0]))
