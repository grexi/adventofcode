inp = open("input.txt", "r").readlines()


graph = {}
reverse_graph = {}
nodes = set()
childnodes = set()
for l in inp:
    #Step G must be finished before step X can begin.
    parts = l.split(" ")
    left = parts[1]
    right = parts[7]
    nodes.add(left)
    nodes.add(right)
    childnodes.add(right)
    if left not in graph:
        graph[left] = []
    graph[left].append(right)
    if right not in reverse_graph:
        reverse_graph[right] = []
    reverse_graph[right].append(left)


def unlock(path, visited, graph, reverse_graph, n, next_nodes):
    path.append(n)
    visited.add(n)
    if n in graph:
        for x in graph[n]:
            available = True
            if x in reverse_graph:
                for y in reverse_graph[x]:
                    if y not in visited:
                        available = False
            if available:
                next_nodes.append(x)
        
        next_nodes.sort()
        
def part1(graph, reverse_graph, nodes, childnodes):
    roots = list(nodes.difference(childnodes))
    roots.sort()

    path = []    
    next_nodes = roots
    visited = set()
    while len(next_nodes) > 0:
        #print("Available %r " % next_nodes)
        n = next_nodes.pop(0)
        
        if n in visited:
            continue
        #print("Take %r" % n)
        unlock(path, visited, graph, reverse_graph, n, next_nodes)

    return "".join(path)
    


def part2(graph, reverse_graph, nodes, childnodes):
    sec = 0

    roots = list(nodes.difference(childnodes))
    roots.sort()

    path = []    
    next_nodes = roots
    visited = set()
    workers = [ ['-', 0] , ['-',0], ['-',0], ['-',0], ['-',0]]

    def get_duration(task):
        return ord(task)-64 +60

    while True:
        free_workers = []
        for i in xrange(len(workers)):
            if workers[i][1] > 0:
                workers[i][1] -= 1
                if workers[i][1] == 0:
                    unlock(path, visited, graph, reverse_graph, workers[i][0], next_nodes)
                    workers[i][0] = '-'
                    free_workers.append(i)
            else:
                free_workers.append(i)

        
        for i in free_workers:
            if len(next_nodes) > 0:
                n = next_nodes.pop(0)        
                workers[i] = [n, get_duration(n)]
        
        sec +=1
        totalsum = 0
        for i in xrange(len(workers)):
            totalsum += workers[i][1]
        if totalsum == 0:
            break


    return sec-1

print(part1(graph, reverse_graph, nodes, childnodes))
print(part2(graph, reverse_graph, nodes, childnodes))