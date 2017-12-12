sample = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

def build_graph(connections):
    graph = {}
    for conn in connections:
        p = conn.strip().split(" ")
        if p[0] not in graph:
            graph[p[0]] = set()
        cns = p[2:]
        for c in cns:
            graph[p[0]].add(c.strip(", "))

    return graph

def reachable_nodes(graph, start):
    seen = set()
    to_check = set(graph[start])
    seen.add(start)
    while len(to_check) > 0:
        for n in to_check:
            seen.add(n)
            to_check = to_check.union(graph[n])
        to_check = to_check.difference(seen)
    return seen
    
def sccs(graph):
    already_seen = set()
    scc = 0
    for n in graph:
        if n in already_seen:
            continue
        already_seen = already_seen.union(reachable_nodes(graph, n))
        scc += 1
    return scc
    
graph = build_graph(sample.split("\n"))
print(len(reachable_nodes(graph, '0')))
print(sccs(graph))
graph2 = build_graph(open("input.txt", "r").readlines())
print(len(reachable_nodes(graph2, '0')))
print(sccs(graph2))
