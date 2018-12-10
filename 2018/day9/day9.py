from Queue import deque

def marblegame(player, marbles):
    currentMarble = 1
    currentPlayer = 0
    mar = deque()
    mar.append(0)

    scores = [0 for _ in xrange(player)]

    while currentMarble <= marbles+1:
        if currentMarble % 23 == 0:
            scores[currentPlayer] += currentMarble
            mar.rotate(-7)
            scores[currentPlayer] += mar.pop()            
        else:
            mar.rotate(2)
            mar.append(currentMarble)

        currentMarble += 1
        currentPlayer = (currentPlayer +1 ) % player
    return max(scores)


print(marblegame(9, 25))    
print(marblegame(10, 1618))
print(marblegame(13, 7999))
print(marblegame(17, 1104))

print(marblegame(470, 72170))
print(marblegame(470, 7217000))