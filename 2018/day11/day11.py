def get_power_level(x,y, serial):
    rackid = (x+1) + 10
    power_level = rackid * (y+1)
    power_level += serial
    power_level *= rackid
    hundreds = 0
    if power_level >= 100:
        hundreds = int(str(power_level)[-3])
    return hundreds - 5


#print get_power_level(121, 78, 57)
#print get_power_level(216, 195, 39)
#print get_power_level(100, 152, 71)

def build_cells(serial):
    cells = []
    for i in range(300):
        row = []
        for j in range(300):
            row.append(get_power_level(j, i, serial))
        cells.append(row)
    return cells



def power(cells, x, y, square):
    psum = 0
    for i in range(square):
        for j in range(square):
            psum += cells[x+i][y+j]
    return psum

def find_max(cells, square=3):
    max_power = -1
    max_coords = None
    for i in range(300-square+1):
        for j in range(300-square+1):
            p = power(cells, i, j, square)
            if p > max_power:
                max_power = p
                max_coords = (i, j, square)
    
    return max_power, max_coords

def find_largest_square(cells):
    max_p = -1
    max_c = None
    for i in range(1,301):
        print(i, max_p, max_c)    
        max_power, max_coords = find_max(cells, i)
        if max_power > max_p:
            max_p = max_power
            max_c = max_coords
    return max_p, max_c


cells = build_cells(8868)

max_power, max_coords = find_max(cells)
print "Power %r, %d,%d,%d" % (max_power, max_coords[1]+1, max_coords[0]+1, max_coords[2])

max_power2, max_coords2 =  find_largest_square(cells)
print "Power %r, %d,%d,%d" % (max_power2, max_coords2[1]+1, max_coords2[0]+1, max_coords2[2])