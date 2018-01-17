machine = [0 for x in xrange(10240)]

index = 0
state = 'A'
for i in xrange(12794428):
	if state == 'A':
		if machine[index] == 0:
			machine[index] = 1
			index += 1
			state = 'B'
		else:
			machine[index] = 0
			index -= 1
			state = 'F'
	elif state == 'B':
		if machine[index] == 0:
			machine[index] = 0
			index += 1
			state = 'C'
		else:
			machine[index] = 0
			index += 1
			state = 'D'
	elif state == 'C':
		if machine[index] == 0:
			machine[index] = 1
			index -= 1
			state = 'D'
		else:
			machine[index] = 1
			index += 1
			state = 'E'
	elif state == 'D':
		if machine[index] == 0:
			machine[index] = 0
			index -= 1
			state = 'E'
		else:
			machine[index] = 0
			index -= 1
			state = 'D'
	elif state == 'E':
		if machine[index] == 0:
			machine[index] = 0
			index += 1
			state = 'A'
		else:
			machine[index] = 1
			index += 1
			state = 'C'
	elif state == 'F':
		if machine[index] == 0:
			machine[index] = 1
			index -= 1
			state = 'A'
		else:
			machine[index] = 1
			index += 1
			state = 'A'

print(sum(machine))
