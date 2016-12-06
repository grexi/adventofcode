
import re
import operator
import string

def room(room):
    match = re.match("(.*)\[(.*)\]", room).groups()
    checksum = match[1]
    parts = match[0].split("-")
    roomid = int(parts[-1])
    parts = "".join(parts[:-1])
    vals = {}
    for s in parts:
        if s in vals:
            vals[s] += 1
        else:
            vals[s] = 1


    def sort_extract(val):
        return (val[1]*-1, val[0])
    sort_vals = sorted(vals.items(), key=sort_extract)
    my_checksum = "".join([x for (x,y) in sort_vals][:5])
    #print ("%r" % sort_vals)
    #print("vals %r checksum %r sort_vals %r" % (vals, checksum, my_checksum))
    if checksum != my_checksum:
        return 0
    else:
        return roomid

def decrypt(room):
    match = re.match("(.*)\[(.*)\]", room).groups()
    checksum = match[1]
    parts = match[0].split("-")
    roomid = int(parts[-1])
    parts = "".join(parts[:-1])

    out = []
    for l in parts:
        if l == "-":
            out.append(" ")
        else:
            pos = string.lowercase.find(l) 
            out.append(string.lowercase[(pos+roomid) % 26])

    print("%r %r" % ("".join(out), roomid))

#print room("aaaaa-bbb-z-y-x-123[abxyz]")
#print room("a-b-c-d-e-f-g-h-987[abcde]")
#print room("not-a-real-room-404[oarel]")
#print room("totally-real-room-200[decoy]")

if __name__ == "__main__":
    infile = open("day4/input.txt")
    total = 0
    for line in infile.readlines():
        total += room(line)
        decrypt(line)
    print("Total: %r" % total)
