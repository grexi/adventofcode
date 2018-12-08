tree = [int(x) for x in open("input.txt", "r").read().split(' ')]

"2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
print tree

def parse_tree(index, tree):
    child_count = tree[index]
    metadata_count = tree[index+1]

    mylength = 2
    
    metadata_sum = 0
    for i in xrange(child_count):
        clen, cmeta = parse_tree(index + mylength, tree)
        mylength += clen
        metadata_sum += cmeta

    
    for j in xrange(metadata_count):
        metadata_sum += tree[index+mylength+j]
    mylength += metadata_count
    return mylength, metadata_sum

print parse_tree(0, tree)


def parse_tree2(index, tree):
    child_count = tree[index]
    metadata_count = tree[index+1]

    mylength = 2
    myvalue = 0
    metadata_sum = 0
    child_values = []
    for i in xrange(child_count):
        clen, cmeta, value = parse_tree2(index + mylength, tree)
        mylength += clen
        metadata_sum += cmeta
        child_values.append(value)

    
    for j in xrange(metadata_count):
        meta = tree[index+mylength+j]
        metadata_sum += meta
        if meta <= len(child_values):
            myvalue += child_values[meta-1]
    mylength += metadata_count

    if child_count == 0:
        myvalue = metadata_sum
    

    return mylength, metadata_sum, myvalue

print parse_tree2(0, tree)