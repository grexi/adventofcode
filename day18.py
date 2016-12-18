def generate_tiles(start, rows):
    floor = [start]
    for i in range(rows-1):
        f = []
        for j in range(len(start)):
            if j>=1:
                l = floor[i][j-1]
            else:
                l = "."
            c = floor[i][j]
            if j<len(start)-1:
                r = floor[i][j+1]
            else:
                r = "."
            if (l,c,r) == ('^', '^',".") or (l,c,r) == (".", "^", "^") or \
                (l,c,r) == ("^", ".", ".") or (l,c,r) == (".", ".", "^"):
                f.append("^")
            else:
                f.append(".")
            
        floor.append("".join(f))
    return floor
def safe_tiles(floor):
    cnt = 0
    for f in floor:
        cnt += f.count(".")
    return cnt


print(safe_tiles(generate_tiles(".^^.^.^^^^", 10)))
print(safe_tiles(generate_tiles("......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 40)))

print(safe_tiles(generate_tiles("......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..", 400000)))
