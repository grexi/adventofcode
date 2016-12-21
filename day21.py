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

	for ins in instr:
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

	return "".join(start)

def reverse_scramble_brute(start, instr):
	for inputs in permutations("abcdefgh"):
		if scramble(inputs, instr) == start:
			return inputs
	return False

def reverse_scramble(start, instr):
	start = [s for s in start]

	for ins in reversed(instr):
		#print("%r %r" % (start, ins))
		ins = ins.strip().split()
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
				steps = 1 + lpos
				if lpos >= 4:
					steps += 1
				steps = steps % len(start)
				start = rotate(start, steps)
		elif ins[0] == "reverse":
			x = int(ins[2])
			y = int(ins[4])
			start = reverse(start, x, y)
		elif ins[0] == "move":
			x = int(ins[2])
			y = int(ins[5])
			start = move(start, y, x)

	return "".join(start)

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

print(scramble("abcde", instrs))


f = open("day21/input.txt", "r")
instructions = f.readlines()
print(scramble("abcdefgh", instructions))
print(reverse_scramble("fbgdceah", instructions))
print(reverse_scramble_brute("fbgdceah", instructions))

