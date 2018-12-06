inp = open("input.txt", "r").readlines()
coords = []
maxx = 0
maxy = 0
for i in inp:
    p = i.strip().split(",")
    x = int(p[0])
    y = int(p[1])
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    coords.append( (x, y ) ) 

#print coords, maxx, maxy

edge_coords = set()

coord_count = {}
regsum = 0
for i in xrange(maxx+1):
    for j in xrange(maxy+1):
        mindist = 10000000
        mincoord = None
        dists = []
        for coord in coords:
            dist = abs(i-coord[0]) + abs(j-coord[1])
            if dist < mindist:
                mindist = dist
                mincoord = coord
            dists.append(dist)
        if dists.count(mindist) == 1:
            if mincoord not in coord_count:
                coord_count[mincoord] = 0
            coord_count[mincoord] += 1

            if i == 0 or j == 0 or i == maxx or j == maxy:
                edge_coords.add(mincoord)
        
        if sum(dists) < 10000:
            regsum += 1

max_area = 0
for c in coord_count:
    if c in edge_coords:
        continue
    if coord_count[c] > max_area:
        max_area = coord_count[c]

print max_area, regsum
