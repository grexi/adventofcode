import re
matcher = re.compile("p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>")
def parse_particle(line):
	p = { "x": 0, "y": 0, "z": 0, "vx": 0, "vy": 0, "vz":0, "ax": 0, "ay": 0, "az": 0 }

	g = matcher.match(line).groups()
	p["x"] = int(g[0])
	p["y"] = int(g[1])
	p["z"] = int(g[2])
	p["vx"] = int(g[3])
	p["vy"] = int(g[4])
	p["vz"] = int(g[5])
	p["ax"] = int(g[6])
	p["ay"] = int(g[7])
	p["az"] = int(g[8])
	return p

def dist(p):
	return abs(p["x"]) + abs(p["y"]) + abs(p["z"])

def equal(p1, p2):
	return p1["x"] == p2["x"] and p1["y"] == p2["y"] and p1["z"] == p2["z"]

particles = []
for l in open("input.txt", "r").readlines():
	particles.append(parse_particle(l))

skips = []
it = 0
collisions = set()
l = len(particles)
for c in range(1000):
	for i in xrange(l):
		p = particles[i]
		p["vx"] += p["ax"]
		p["vy"] += p["ay"]
		p["vz"] += p["az"]
		p["x"] += p["vx"]
		p["y"] += p["vy"]
		p["z"] += p["vz"]

	for i in xrange(l):
		if i in collisions:
			continue
		p1 = particles[i]
		for j in xrange(i, l):
			if i == j or j in collisions:
				continue
			p2 = particles[j]
			if equal(p1, p2):
				collisions.add(i)
				collisions.add(j)

mindist = 1e30
i = 0
for p in particles:	
	p["d"] = dist(p)

	if p["d"] < mindist:
		mindist = p["d"]
		minpart = i
	i+=1
		
print("Mindist = %r Particle = %r" % (mindist, minpart))
print("Leftover: %r" % (len(particles) - len(collisions)))

	
