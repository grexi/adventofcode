inp = open("input.txt", "r").readlines()


guardsleeps = {}

import re

logre = re.compile("\[(\d+)-(\d+)-(\d+) (\d\d):(\d\d)\] (.+)")
guardre = re.compile("Guard #(\d+) begins shift")

currentGuard = -1
currentAwake = -1
for line in sorted(inp):
    parts = logre.match(line).groups()
    guardmatches = guardre.match(parts[-1])

    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    hour = int(parts[3])
    minute = int(parts[4])

    action = parts[5]
    if guardmatches:
        currentGuard = int(guardmatches.groups()[0])

    if currentGuard not in guardsleeps:
        guardsleeps[currentGuard] = []
    
    if action == "falls asleep":
        guardsleeps[currentGuard].append( { "d": "%s-%s" % (month, day), "m": minute})
    elif action == "wakes up":
        guardsleeps[currentGuard].append( { "d": "%s-%s" % (month, day), "m": minute})


guardstats = {}
grand_total = 0
sleeperguard = -1
for guard in guardsleeps:
    total = 0
    minutes = {}
    for i in xrange(0, len(guardsleeps[guard]), 2):
        for j in xrange(guardsleeps[guard][i]["m"], guardsleeps[guard][i+1]["m"]):
            total += 1
            if j not in minutes:
                minutes[j] = 0
            minutes[j] += 1
    guardstats[guard] = { "total": total, "minutes": minutes}
    if total > grand_total:
        grand_total = total
        sleeperguard = guard


max_minutes = 0
max_minute = -1
for m in guardstats[sleeperguard]["minutes"]:
    if guardstats[sleeperguard]["minutes"][m] > max_minutes:
        max_minutes = guardstats[sleeperguard]["minutes"][m]
        max_minute = m

sleeperguard2 = -1
max_minutes2 = 0
max_minute2 = -1
for g in guardstats:
    for m in guardstats[g]["minutes"]:
        if guardstats[g]["minutes"][m] > max_minutes2:
            max_minutes2 = guardstats[g]["minutes"][m]
            max_minute2 = m
            sleeperguard2 = g

print("Sleeper Guard %r Sleeps at minute %r = %r" % (sleeperguard, max_minute, sleeperguard*max_minute))

print("Sleeper Guard %r Sleeps at minute %r = %r" % (sleeperguard2, max_minute2, sleeperguard2*max_minute2))

