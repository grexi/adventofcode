
def pos(number):
	i = 0
	x,y = 0, 0
	
	max_x, min_x, max_y, min_y = 0,0,0,0
	dire = "R"
	while i < number-1:
		#print "%s= (%s,%s)" % (i+1, x,y)		
		if dire == "R":
			dx = 1
			dy = 0
		elif dire == "L":
			dx = -1
			dy = 0
		elif dire == "U":
			dx = 0
			dy = 1
		elif dire == "D":
			dx = 0
			dy = -1

		x += dx
		y += dy
		i += 1	
		if x > max_x:
			max_x = x
			dire = "U"
		if x < min_x:
			min_x = x
			dire = "D"
		if y > max_y:
			max_y = y
			dire = "L"
		if y < min_y:
			min_y = y
			dire = "R"

	return abs(x)+abs(y)

def sums(number):
	i = 0
	x,y = 0, 0
	
	max_x, min_x, max_y, min_y = 0,0,0,0
	dire = "R"

	j = -1
	dim = 0
	while dim < number:
		j+=2
		dim = j**2		
	
	field = []
	for k in range(j):
		field.append([-1 for _ in range(j)])

	field[0][0] = 1
	while i < number-1:
		#print "%s= (%s,%s)" % (i+1, x,y)		
		if dire == "R":
			dx = 1
			dy = 0
		elif dire == "L":
			dx = -1
			dy = 0
		elif dire == "U":
			dx = 0
			dy = 1
		elif dire == "D":
			dx = 0
			dy = -1
			
		prevsum = 0
		if field[x-1][y-1] != -1:
			prevsum += field[x-1][y-1]
		if field[x-1][y] != -1:
			prevsum += field[x-1][y]
		if field[x-1][y+1] != -1:
			prevsum += field[x-1][y+1]

		if field[x][y-1] != -1:
			prevsum += field[x][y-1]
		if field[x][y] != -1:
			prevsum += field[x][y]
		if field[x][y+1] != -1:
			prevsum += field[x][y+1]

		if field[x+1][y-1] != -1:
			prevsum += field[x+1][y-1]
		if field[x+1][y] != -1:
			prevsum += field[x+1][y]
		if field[x+1][y+1] != -1:
			prevsum += field[x+1][y+1]

		if field[x][y] == -1:
			field[x][y] = prevsum
		if prevsum > number:
			return prevsum
		x += dx
		y += dy
		i += 1	
		if x > max_x:
			max_x = x
			dire = "U"
		if x < min_x:
			min_x = x
			dire = "D"
		if y > max_y:
			max_y = y
			dire = "L"
		if y < min_y:
			min_y = y
			dire = "R"


print(pos(1))
print(pos(12))
print(pos(23))
print(pos(1024))
print(pos(361527))

print(sums(361527))
