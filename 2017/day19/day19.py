sample = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+"""

def follow(matrix):
	seen = []

	curpos = [0, 0]
	curdir = "d"
	i = 0
	for c in matrix[0]:
		if c == '|':
			curpos = [i, 0]
			break
		i += 1
	steps = 0
	while True:

		if matrix[curpos[1]][curpos[0]] not in "-+| ":
			seen.append(matrix[curpos[1]][curpos[0]])

		if matrix[curpos[1]][curpos[0]] == '+':
			if curdir != "l" and len(matrix[curpos[1]]) > curpos[0]+1 and matrix[curpos[1]][curpos[0]+1] != ' ':
				curdir = "r"
			elif curdir != "r" and curpos[0]-1 >= 0 and matrix[curpos[1]][curpos[0]-1] != ' ':
				curdir = "l"
			elif curdir != "d" and curpos[1]-1 >= 0 and matrix[curpos[1]-1][curpos[0]] != ' ':
				curdir = "u"
			elif curdir != "u" and len(matrix) > curpos[1]+1 and matrix[curpos[1]+1][curpos[0]] != ' ':
				curdir = "d"
		elif matrix[curpos[1]][curpos[0]] == ' ':
			break
		if curdir == "d":
			curpos[1] += 1
		elif curdir == "u":
			curpos[1] -= 1
		elif curdir == "r":
			curpos[0] += 1
		elif curdir == "l":
			curpos[0] -= 1
		steps +=1
	print("".join(seen), steps)

samplem = [[x for x in line] for line in sample.split("\n")]
follow(samplem)
			
puzzlem = [[x for x in line] for line in open("input.txt", "r").readlines()]
follow(puzzlem)

			

