inp = open("input.txt", "r")

field = []
carts = []
for i in inp:    
    row = [x for x in i]
    field.append(row)

for y, r in enumerate(field):
    for x, c in enumerate(r):
        if c in ('>', '^', 'v', '<'):
            cart = { 'x': x, 'y': y, 'dir': c, 'turn': 0, 'crash': False} 
            carts.append(cart)
            if c in ('>', '<'):
                r[x] = "-"
            else:
                r[x] = "|"

def check_collision(carts):   
    for c1 in carts:
        if c1['crash']: 
            continue
        for c2 in carts:
            if c2['crash']: 
                continue
            if c1 != c2:
                if c1['x'] == c2['x'] and c1['y'] == c2['y']:
                    c1['crash'] = True
                    c2['crash'] = True
                    return (c1, c2)                   
    return None
    

def get_next_dir(c):
    dirs = ['<', '^', '>', 'v']
    d = c['dir']
    i = dirs.index(d)
    if c['turn'] == 0:
        c['dir'] = dirs[i-1]
        c['turn'] = 1
    elif c['turn'] == 1:
        c['turn'] = 2
    elif c['turn'] == 2:
        c['dir'] = dirs[(i+1)%4]
        c['turn'] = 0        
    return c

def move_cart(f, c):
    d = c['dir'] 
    if d == '>':
        next = f[c['y']][c['x']+1]
        c['x'] += 1
        if next == '-':
            pass
        elif next == '/':
            c['dir'] = '^'
        elif next == '\\':
            c['dir'] = 'v'
        elif next == '+':
            get_next_dir(c)
    elif d == 'v':
        next = f[c['y']+1][c['x']]
        c['y'] += 1
        if next == '|':
            pass
        elif next == '/':
            c['dir'] = '<'
        elif next == '\\':
            c['dir'] = '>'
        elif next == '+':
            get_next_dir(c)
    elif d == '<':
        next = f[c['y']][c['x']-1]
        c['x'] -= 1
        if next == '-':
            pass
        elif next == '/':
            c['dir'] = 'v'
        elif next == '\\':
            c['dir'] = '^'
        elif next == '+':
            get_next_dir(c)
    elif d == '^':
        next = f[c['y']-1][c['x']]
        c['y'] -= 1
        if next == '|':
            pass
        elif next == '/':
            c['dir'] = '>'
        elif next == '\\':
            c['dir'] = '<'
        elif next == '+':
            get_next_dir(c)

def print_field(field):
    for r in field:
        print "".join(r)

colls = check_collision(carts)
while not colls:
    carts.sort(key = lambda c: (c['y'], c['x']))
    for c in carts:
        if c['crash']:
            continue
        move_cart(field, c)
        colls = check_collision(carts)
        if colls:
            break
        #print_field(field)
    


print "%s,%s" % (colls[0]['x'], colls[0]['y'])


steps = 0
while len(carts) > 1:
    
    carts = [cart for cart in carts if not cart['crash']]
    carts.sort(key = lambda c: (c['y'], c['x']))
    for c in carts:
        steps +=1
        if c['crash']:
            continue
        move_cart(field, c)
        colls = check_collision(carts)
        
        
print(steps)        
print("Last cart %s,%s" % (carts[0]['x'], carts[0]['y']))