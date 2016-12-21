from itertools import permutations


def swap_xy(start, x,y):
	t = start[x]
	start[x] = start[y]
	start[y] = t	
	return start

def rotate(start, steps):
	return  start[steps:] + start[:steps]

def reverse(start, x, y):
	before = start[:x]
	after = start[y+1:]
	between = start[x:y+1]
	return before+ between[::-1] + after
	
def move(start, x, y):
	t = start[x]
	start = start[:x] + start[x+1:]
	start = start[:y] + [t] + start[y:]
	return start

def scramble(start, instr):
	start = [s for s in start]
	intermediate = []

	for ins in instr:
		intermediate.append(["".join(start), ins])
		#print("%r %r" % (start, ins))
		ins = ins.strip().split()
		if ins[0] == "swap":
			if ins[1] == "position":
				x = int(ins[2])
				y = int(ins[5])
				start = swap_xy(start,x,y)
			elif ins[1] == "letter":
				lx = ins[2]
				ly = ins[5]
				x = start.index(lx)
				y = start.index(ly)
				start = swap_xy(start,x,y)
		elif ins[0] == "rotate":

			if ins[1] == "left":
				steps = int(ins[2])
				steps = steps % len(start)
				start = rotate(start, steps)
			elif ins[1] == "right":
				steps = int(ins[2])
				steps = steps % len(start)
				start = rotate(start, -steps)
			elif ins[1] == "based":
				letter = ins[6]
				lpos = start.index(letter)
				steps = 1 + lpos
				if lpos >= 4:
					steps += 1
				steps = steps % len(start)
				start = rotate(start, -steps)
		elif ins[0] == "reverse":
			x = int(ins[2])
			y = int(ins[4])
			start = reverse(start, x, y)
		elif ins[0] == "move":
			x = int(ins[2])
			y = int(ins[5])
			start = move(start, x, y)

	return "".join(start), intermediate

def reverse_scramble_brute(start, instr):
	for inputs in permutations("abcdefgh"):
		if scramble(inputs, instr)[0] == start:
			return "".join(inputs)
	return False

def reverse_scramble(start, instr):
	start = [s for s in start]
	intermediate = []

	for inss in reversed(instr):

		#print("%r %r" % (start, inss))
		ins = inss.strip().split()
		if ins[0] == "swap":
			if ins[1] == "position":
				x = int(ins[2])
				y = int(ins[5])
				start = swap_xy(start,y,x)
			elif ins[1] == "letter":
				lx = ins[2]
				ly = ins[5]
				x = start.index(lx)
				y = start.index(ly)
				start = swap_xy(start,y,x)
		elif ins[0] == "rotate":

			if ins[1] == "left":
				steps = int(ins[2])
				steps = steps % len(start)
				start = rotate(start, -steps)
			elif ins[1] == "right":
				steps = int(ins[2])
				steps = steps % len(start)
				start = rotate(start, steps)
			elif ins[1] == "based":
				letter = ins[6]
				lpos = start.index(letter)
				inv = { 1: 1, 2: -2, 3: -6, 6: 0, 7: 4, 0: 1, 5: -5, 4: -1}
				#steps = lpos - 1
				#if lpos >= 4:
				#	steps -= 1
				#steps = steps % len(start)
				start = rotate(start, inv[lpos])
		elif ins[0] == "reverse":
			x = int(ins[2])
			y = int(ins[4])
			start = reverse(start, x, y)
		elif ins[0] == "move":
			x = int(ins[2])
			y = int(ins[5])
			start = move(start, y, x)
		intermediate.append(["".join(start), inss])
	return "".join(start), intermediate

instrs = [
"swap position 4 with position 0",
"swap letter d with letter b",
"reverse positions 0 through 4",
"rotate left 1 step",
"move position 1 to position 4",
"move position 3 to position 0",
"rotate based on position of letter b",
"rotate based on position of letter d"
]

#print(scramble("abcde", instrs))
#print(reverse_scramble("decab", instrs))

#sys.exit()
f = open("day21/input.txt", "r")
instructions = f.readlines()
res, im1 = scramble("abcdefgh", instructions)
print(res)
res2, im2 = reverse_scramble("fbgdceah", instructions)
im1.reverse()
print res2
for i in range(len(im2)):
	print("%r %r %r" % (im1[i][0] == im2[i][0], im1[i], im2[i]))

if False:
	for inputs in permutations("abcdefgh"):
		if reverse_scramble(scramble(inputs, instructions)[0], instructions)[0] != "".join(inputs):
			print("%r does not work" % ("".join(inputs)))



#print(reverse_scramble("fbgdceah", instructions)[0])
#print(reverse_scramble_brute("fbgdceah", instructions))

