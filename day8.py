screen = [ [" " for i in range(50)] for j in range(6)]

def print_screen(scr):
    for line in screen:
        print("|%s|" % ("".join(line)))

def count_screen(scr):
    cnt = 0
    for l in screen:
        for c in l:
            if c == '#':
                cnt+=1
    return cnt

print_screen(screen)

def adapt_screen(screen, command):
    parts = command.split()
    if parts[0] == "rect":
        x, y = map(int, parts[1].split("x"))
        for i in range(x):
            for j in range(y):
                screen[j][i] = "#"
    elif parts[0] == "rotate" and parts[1] == "column":
        x = int(parts[2].split("=")[1])
        cnt = int(parts[4])
        for c in range(cnt):
            tmp = screen[5][x]
            screen[5][x] = screen[4][x]
            screen[4][x] = screen[3][x]
            screen[3][x] = screen[2][x]
            screen[2][x] = screen[1][x]
            screen[1][x] = screen[0][x]
            screen[0][x] = tmp
    elif parts[0] == "rotate" and parts[1] == "row":
        y = int(parts[2].split("=")[1])
        cnt = int(parts[4])
        screen[y] = screen[y][-cnt:] + screen[y][:-cnt]


test = False
if test == True:
    adapt_screen(screen, "rect 3x10")
    print_screen(screen)
    adapt_screen(screen, "rotate column x=1 by 1")
    print_screen(screen)
    adapt_screen(screen, "rotate row y=0 by 4")
    print_screen(screen)
    adapt_screen(screen, "rotate column x=1 by 1")

    print_screen(screen)

if test == False:
        r = open("day8/input.txt", "r")

        for line in r.readlines():
            print(line)
            adapt_screen(screen, line)
        print_screen(screen)
        print("Count: %r" %count_screen(screen))
