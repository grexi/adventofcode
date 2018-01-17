sample = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""


def parse_bridges(lines):
	bridges = []
	connections = {}
	i = 0
	for l in lines:
		b = l.strip()

		p = tuple((int(x) for x in b.split("/")))
		bridges.append(p)
		if p[0] not in connections:
			connections[p[0]] = set()
		if p[1] not in connections:
			connections[p[1]] = set()
		connections[p[0]].add(i)
		connections[p[1]].add(i)
		i += 1
	return bridges, connections

#bridges, connections = parse_bridges(sample.split("\n"))
bridges, connections = parse_bridges(open("input.txt","r").readlines())


max_sum = 0
max_length = 0
def find_max(bridges, connections, start, used_bridges):
	global max_sum, max_length
	next_conns = connections[start]
	
	found = False

	for c in next_conns:
		next_bridge = bridges[c]
		if c in used_bridges:
			continue
		found = True
		#print("%r" % (bridges[c],))
		if next_bridge[0] == start:
			s = find_max(bridges, connections, next_bridge[1], used_bridges.union(set((c,))))
		else:
			s = find_max(bridges, connections, next_bridge[0], used_bridges.union(set((c,))))


	if not found:

		if len(used_bridges) >= max_length:
			if max_length < len(used_bridges):
				max_length = len(used_bridges)
				max_sum = 0
			s = 0			
			for x in used_bridges:
				s += bridges[x][0] + bridges[x][1]
			#print("End %r " % s)
		
			if s > max_sum:
				max_sum = s
		return max_sum		


	
find_max(bridges, connections, 0, set())
print(max_sum, max_length)
