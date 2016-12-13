import copy
import json
import hashlib
import sys 
import cPickle
from Queue import PriorityQueue
import time

def find_possible_steps(world):
    steps = []

    E = world["E"]
    FL = set(world["F"][E])
    FL.add("-")

    # elevator down:
    if E != 0:    
        for el_x in FL: 
            for el_y in FL:
                if el_x != el_y:
                    mixedel = set([x for x in [el_x, el_y] if x != '-'])
                    if is_allowed(world, mixedel, E-1, True) and is_allowed(world, mixedel, E, False):
                        steps.append((mixedel, -1))

    # elevator up:
    if E != len(world["F"])-1:
        for el_x in FL:
            for el_y in FL:
                if el_x != el_y:
                    mixedel = set([x for x in [el_x, el_y] if x != '-'])
                    if is_allowed(world, mixedel, E+1, True) and is_allowed(world, mixedel, E, False):
                        steps.append((mixedel, +1))


    #steps.sort()            

    def comparer(x,y):
        return x[1]*len(x[0])-y[1]*len(y[0])
    steps.sort(cmp=comparer, reverse=True)
    last = None
    retsteps = []
    for s in steps:
        if s != last:
            retsteps.append(s)
        last = s
    return retsteps                                     
  
debug = False
visits = {}     
solutions = []

def find_path(world, max_depth=100):
    global solutions
    global debug

    global visits

    i = 0
    last = time.time()
    #print ("looking at world, step %r" % steps)
    to_visit = PriorityQueue()
    to_visit.put((0, 0, world))
    while not to_visit.empty():
        prio, steps, world = to_visit.get()
        i+=1
        if i%100000 == 0:
            dur = time.time() - last
            print("%.2f iterations / sec " % (100000/dur))
            print("%s[%d] %s State %r %r" % (" "*steps, to_visit.qsize(), steps, world["E"], world["F"]))
            last = time.time()
        if debug:
            print("%s[%d] %s State %r %r" % (" "*steps, to_visit.qsize(), steps, world["E"], world["F"]))
        #print("%r" % world)
        worldS = "%s:%s" % (world["E"], ",".join((str(x) for x in world["F"]))) 
        #json.dumps(world)
        
        #worldS = cPickle.dumps(world, -1) 
        if worldS in visits and visits[worldS] <= steps:
            if debug:
                print("%sAlready been here." % (" "*steps))
            continue
        visits[worldS] = steps
        poss_steps = find_possible_steps(world)
        if debug:
            print("possible %r" % poss_steps)
        for step in poss_steps:
            
            if debug:
                print("%s[%r], possible: %r" % (" "*steps, steps, step))
                    
            #w = cPickle.loads(cPickle.dumps(world, -1))
            w = { "F": [], "E": world["E"], "parent": world }
            for f in world["F"]:
                w["F"].append(set(f))
            srcE = w["E"]
            w["E"] += step[1]
            trgE = w["E"]
            for el in step[0]:
                #print("%r %r" % (el, step[1]))
                w["F"][srcE].remove(el)
                #w["F"][srcE].sort()
                w["F"][trgE].add(el)
                #w["F"][trgE].sort()
            if debug:
                print("%s - State %r" % (" "*steps, w))
            if is_goal(w):
                print("%r Found solution! with %r steps considering %r nodes" % (step, steps+1, i))
                solutions.append(steps+1)
                solutions.sort()
                manual_steps = []
                st = w
                while st:
                    manual_steps.append(st)
                    st = st["parent"]
                manual_steps.reverse()
                for mw in manual_steps:
                    print("%s:%s" % (mw["E"], ",".join((str(x) for x in mw["F"]))))
                print "="*80
                return
            else:
                if steps <= max_depth:
                    #print("%r" % to_visit)
                    exCost = len(w["F"][0])*3 + len(w["F"][1])*2 + len(w["F"][2])*1
                    to_visit.put((steps+exCost, steps+1, w))



        


def is_allowed(world, elements, floor, add):
    if add:
        allelems = world["F"][floor].union(elements) 
    else:
        allelems = world["F"][floor].difference(elements) 

    for el in allelems:
        if el[1] == "M":
            if el[0]+"G" in allelems:
                continue
            # either matching generator or no generator
            for x in allelems:
                if x[1] == "G":
                    return False
    return True

def is_goal(world):
    if world["E"] != 3: #len(world["F"])-1:
        return False
    for f in world["F"][:-1]:
        if len(f) != 0:
            return False
    return True

if False:
    print("%r" %is_allowed({
            "F": [ 
            set(["BM", "RM"]),
            [],
            ],
            "E": 3
            }, ["DM"], 0, True))
    sys.exit()
test = False
if test == True:
    world = {
            "F": [ 
            set(["HM", "LM"]),
            set(["HG"]),
            set(["LG"]),
            set([])
            ],
            "E": 0,
            "parent": None
            }

if test == False:
    world = {
            "F": [
            #set(["PG", "PM"]), #v1
            set(["PG", "PM", "EG", "EM", "DG", "DM"]), #v2
            set(["CG", "UG", "RG", "BG"]),
            set(["CM", "UM", "RM", "BM"]),
            []
            ],
            "E": 0,
            "parent": None
            }
start = time.time()
find_path(world)
end = time.time()
print("It took %.2f seconds" % (end-start))
solutions.sort()
print(solutions[0])

