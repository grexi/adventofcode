import md5


shortest = ""
longest = ""
def md5_maze(start, pos):
    #if len(solutions) > 10000:
    #    return
    global solutions, shortest, longest
    #print("Starting at %r %r" % (start, pos))
    if pos[0] == 3 and pos[1] == 3:
        if len(start) < len(shortest) or shortest == "":
            shortest = start
        if len(start) > len(longest):
            longest = start
        return
    # up, down, left, right
    dirs = [(0,-1), (0, 1), (-1, 0), (1, 0)]
    dirStr = ["U", "D", "L", "R"]
    doors = md5.md5(start).hexdigest()[:4]    
    doors = [int(x,16) for x in doors]
    for i in range(4):
        if doors[i] > 10:
            newpos = [pos[0], pos[1]]
            newpos[0] += dirs[i][0]
            newpos[1] += dirs[i][1]
            #print("Going %r from %r to %r" % (dirStr[i], pos, newpos))
            if 0 <= newpos[0] and newpos[0] <= 3 and \
               0 <= newpos[1] and newpos[1] <= 3:
                md5_maze(start+dirStr[i], newpos)

md5_maze("gdjjyniy", [0,0])
l = len("gdjjyniy")
print(shortest[l:])
print(len(longest[l:]))
