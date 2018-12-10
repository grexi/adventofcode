#"position=< 9,  1> velocity=< 0,  2>"
inp = open("input.txt", "r").readlines()
import re
import sys
pointre = re.compile("position=<\s*(\-?\d+),\s*(\-?\d+)> velocity=<\s*(\-?\d+),\s*(\-?\d+)>")
points = []
for i in inp:
    m = pointre.match(i)
    if m:
        g = m.groups()
        p = [int(x) for x in g]
        points.append(p)


def print_points(points, min_x, max_x, min_y, max_y):
    for i in xrange(min_x-1, max_x+1):
        for j in xrange(min_y-1, max_y+1):
            found = False
            for p in points:
                if p[1] == i and p[0] == j:
                    found = True
            if found:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print("-")


#print_points(points, -50, 50, -50, 50)


min_w = 1e10
min_h = 1e10
old_height = min_h
height = 0
seconds = 0
while height < old_height:
    
    old_height = min_h
    min_x = 1e10
    min_y = 1e10
    max_x = 0
    max_y = 0
    for p in points:
        p[0] += p[2]
        p[1] += p[3]
        if p[0] < min_x:
            min_y = p[0]
        elif p[0] > max_x:
            max_y = p[0]
        if p[1] < min_y:
            min_x = p[1]
        elif p[1] > max_y:
            max_x = p[1]
    if abs(max_x - min_x) < min_w:
        min_w  = abs(max_x - min_x)
    if abs(max_y - min_y) < min_h:
        min_h = abs(max_y - min_y)
    old_height = min_h
    
    seconds += 1
    if old_height == 21:
    #if seconds > 10075:
        print_points(points, min_x-5, max_x+5, min_y-25, max_y+25)
        break

print seconds  
