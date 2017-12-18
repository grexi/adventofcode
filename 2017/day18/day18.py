sample ="""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

def get_val(x, regs):
	try:
		x_i = int(x)
		return x_i
	except:
		if x not in regs:
			regs[x] = 0
		return regs.get(x)

def execute(lines):
	regs = {}
	lastsnd = 0
	pgc = 0
	while True:
		l = lines[pgc].strip()

		p = l.split(" ")
		if p[0] == "snd":
			lastsnd = get_val(p[1], regs)
			pgc += 1
		elif p[0] == "set":
			regs[p[1]] = get_val(p[2], regs)
			pgc += 1
		elif p[0] == "add":
			regs[p[1]] = get_val(p[1], regs) + get_val(p[2], regs)
			pgc += 1
		elif p[0] == "mul":
			regs[p[1]] = get_val(p[1], regs) * get_val(p[2], regs)
			pgc += 1
		elif p[0] == "mod":
			regs[p[1]] = get_val(p[1], regs) % get_val(p[2], regs)
			pgc += 1
		elif p[0] == "rcv":
			x = get_val(p[1], regs)
			if x != 0:
				print("Recover %r" % lastsnd)
				return lastsnd
			pgc += 1
		elif p[0] == "jgz":
			x = get_val(p[1], regs)
			if x > 0:
				off = get_val(p[2], regs)
				pgc += off
			else:
				pgc += 1

print(execute(sample.split("\n")))
l = open("input.txt", "r").readlines()
print(execute(l))


def execute_par(lines, pgmid, inq, outq):
	regs = {}
	regs["p"] = pgmid
	sndcount = 0
	pgc = 0
	while True:
		l = lines[pgc].strip()

		p = l.split(" ")
		if p[0] == "snd":
			outq.put(get_val(p[1], regs))
			sndcount += 1
			if pgmid == 1:
				print("sndcount = %r" % sndcount)
			pgc += 1
		elif p[0] == "set":
			regs[p[1]] = get_val(p[2], regs)
			pgc += 1
		elif p[0] == "add":
			regs[p[1]] = get_val(p[1], regs) + get_val(p[2], regs)
			pgc += 1
		elif p[0] == "mul":
			regs[p[1]] = get_val(p[1], regs) * get_val(p[2], regs)
			pgc += 1
		elif p[0] == "mod":
			regs[p[1]] = get_val(p[1], regs) % get_val(p[2], regs)
			pgc += 1
		elif p[0] == "rcv":
			regs[p[1]] = inq.get()
			pgc += 1
		elif p[0] == "jgz":
			x = get_val(p[1], regs)
			if x > 0:
				off = get_val(p[2], regs)
				pgc += off
			else:
				pgc += 1

import Queue
inq1 = Queue.Queue()
outq1 = Queue.Queue()
import threading 

t1 = threading.Thread(target=execute_par, args=(l, 0, inq1, outq1))
t2 = threading.Thread(target=execute_par, args=(l, 1, outq1, inq1))
t1.start()
t2.start()
t1.join()
t2.join()
