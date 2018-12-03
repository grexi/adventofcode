inp = open("input.txt", "r").readlines()

import re
MAXSIZE = 1000
recte= re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
def parse_rect(line):
    parts = recte.match(line)
    return parts.groups()
    
def print_canvas(canv):
    for l in canv:
        print("".join(("%d" %x for x in l)))
    
def draw_rects(inp):
    dups = 0

    canvas = [[0 for _ in xrange(MAXSIZE)] for _ in xrange(MAXSIZE)]
    rectsizes = {}
    for r in inp:
        rect = parse_rect(r)
        reci = int(rect[0])
        x = int(rect[1])
        y = int(rect[2])
        w = int(rect[3])
        h = int(rect[4])
        rectsizes[reci] = w*h
        
        for i in xrange(w):
            for j in xrange(h):
                if canvas[x+i][y+j] < 0:
                    continue
                if canvas[x+i][y+j] > 0:
                    dups += 1
                    canvas[x+i][y+j] = -1
                else:
                    canvas[x+i][y+j] = reci

    intact = -1
    for r in canvas:
        for c in r:
            if c > 0:
                rectsizes[c] -= 1
             
    for rect in rectsizes:
        if rectsizes[rect] == 0:
            intact = rect
            #print("%r is intact" % rect)
            break;
    #print_canvas(canvas)
    return dups, intact
    
print(draw_rects(inp))


