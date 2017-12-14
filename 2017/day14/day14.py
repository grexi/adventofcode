
def knothash_str(length, string):
    ring = [x for x in range(length)]
    skip = 0
    i = 0
    rotates = []
    for s in string:
        rotates.append(ord(s))
    rotates.extend([17, 31, 73, 47, 23])
    for _ in range(64):
        for rot in rotates:
            part = []
            for j in range(rot):
                part.append(ring[(i+j)%length])
            j = 0
            for p in reversed(part):
                ring[(i+j) % length] = p
                j+=1
            i += skip+rot
            skip += 1

    total_hash = []    
    for x in range(16):
        hashval = 0
        for y in range(16):
            hashval = hashval ^ ring[x*16+y]
        total_hash.append(hashval)        
    return "".join(["%02x" % x for x in total_hash])

def get_ones(hashin):
	return bin(int(hashin,16))

def flood_fill(field, x, y, current_region):
	if x < 0 or y < 0 or x > 127 or y > 127:
		return

	if field[y][x] == '#':
		field[y][x] = current_region
		flood_fill(field, x, y-1, current_region)
		flood_fill(field, x, y+1, current_region)
		flood_fill(field, x-1, y, current_region)
		flood_fill(field, x+1, y, current_region)
	
def get_regions(field):
	current_region = 1
	for y in range(128):
		for x in range(128):
			if field[y][x] == '.':
				continue
			if field[y][x] == '#':
				flood_fill(field, x, y, current_region)
				current_region += 1

	return current_region - 1

testinp = "flqrgnkx"
inp = "amgozmfv"

field = []
sums = 0

for i in range(128):
	line = get_ones(knothash_str(256, "%s-%d" % ( inp, i)))
	sums += line.count("1")
	fieldline = [x == "1" and '#' or '.' for x in line[2:]]
	while len(fieldline) < 128:
		fieldline.insert(0, '.')
	field.append(fieldline)

print("sum of ones = %r" % sums)

print("get_regions %r" % (get_regions(field)))


