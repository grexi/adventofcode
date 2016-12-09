
pos = [1,1]
def bathroom(seq):
	global pos
	codes = [[1,2,3], [4,5,6], [7,8,9]]
	for s in seq:
		if s == "U":
			pos[0] =  max(0, pos[0]-1)
		elif s == "D":
			pos[0] =  min(2, pos[0]+1)
		elif s == "R":
			pos[1] = min(2, pos[1]+1)
		elif s == "L":
			pos[1] = max(0, pos[1]-1)
		#print("%s %r" % (s, pos))
	print(codes[pos[0]][pos[1]]),


pos2 = [2,0]
def bathroom2(seq):
	global pos2
	codes = [[0,  0,  1,  0, 0], 
             [0,  2,  3,  4, 0], 
             [5,  6,  7,  8, 9], 
             [0,"A","B","C", 0],
             [0, 0, "D",  0, 0]]
	for s in seq:
		if s == "U":
			n = max(0, pos2[0]-1)
			if codes[n][pos2[1]] != 0:
				pos2[0] = n 
		elif s == "D":
			n =  min(4, pos2[0]+1)
			if codes[n][pos2[1]] != 0:
				pos2[0] = n 

		elif s == "R":
			n = min(4, pos2[1]+1)
			if codes[pos2[0]][n] != 0:
				pos2[1] = n
		elif s == "L":
			n = max(0, pos2[1]-1)
			if codes[pos2[0]][n] != 0:
				pos2[1] = n
		#print("%s %r" % (s, pos2))
	print(codes[pos2[0]][pos2[1]]),

if False:
	bathroom2("ULL")
	bathroom2("RRDDD")
	bathroom2("LURDL")
	bathroom2("UUUUD")
			 

r = open("day2/input.txt", "r")		

for line in r.readlines():
	bathroom2(line)
