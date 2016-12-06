import md5

def find_hash(start):
    i = 0
    password = []
    while len(password) < 8:
        
        dig = md5.md5("%s%s" % (start,i)).hexdigest()
        if dig[:5] == "00000":
            password.append(dig[5])
        i+= 1
    return "".join(password)

def find_hash2(start):
    i = 0
    password = [".", ".", ".", ".", ".", ".", ".", "."]
    found = 0
    while found < 8:
        
        dig = md5.md5("%s%s" % (start,i)).hexdigest()
        if dig[:5] == "00000":
            pos = int(dig[5], base=16)
            #print "%r %r %r " % (pos, dig[6], password)
            if pos < len(password) and password[pos] == ".":
                password[pos] = dig[6]
                print("\r%s" % "".join(password)),
                found +=1
        i+= 1
    return "".join(password)

print find_hash2("abc")
print find_hash2("reyedfim")
