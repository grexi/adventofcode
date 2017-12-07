sample = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

def build_tree(programs):
	nodes = {
	}
	possible_roots = {}
	child_nodes = {}
	for p in programs:
		parts = p.split("->")
		node_parts = parts[0].split(" ")
		children = None
		if len(parts) > 1:		
			children = [x.strip() for x in parts[1].split(",")]
			for c in children:
				child_nodes[c] = 1
				if c in possible_roots:
					del possible_roots[c]
		node = node_parts[0]
		node_weight = node_parts[1]
		nodes[node] = { "w": int(node_weight.strip().strip("(").strip(")")), "c": children }
		
		
		if node not in child_nodes:
			possible_roots[node] = 1
	return possible_roots, nodes


def calculate_weight(root, nodes):
	if nodes[root]["c"] == None:
		return nodes[root]["w"]
	weights = []

	for c in nodes[root]["c"]:
		w = calculate_weight(c, nodes)
		weights.append(w)

	counts = {}
	balance_w = 0
	for w in weights:
		if w not in counts:
			counts[w] = 0
		counts[w] += 1
		if counts[w] > 1:
			balance_w = w
	
	for w in counts:
		if counts[w] == 1:
			diffindex = weights.index(w)

			diff = balance_w - w
			print("Node is unbalanced: %r child %r differs %r, correct to %r" % (root, nodes[root]["c"][diffindex], diff, nodes[nodes[root]["c"][diffindex]]["w"]+diff))
	s = sum(weights)
	#print "%r = %d + %d = %d" % (root, nodes[root]["w"], s, nodes[root]["w"]+s)
	return s+nodes[root]["w"]

possible_roots, nodes = build_tree(sample.split("\n"))

print(possible_roots.keys()[0])

calculate_weight(possible_roots.keys()[0], nodes)

possible_roots, nodes = build_tree(open("input.txt", "r").readlines())
print(possible_roots.keys()[0])
calculate_weight(possible_roots.keys()[0], nodes)
