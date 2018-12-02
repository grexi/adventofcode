inp = open("input.txt", "r").readlines()

def word_freq(word):
    word = word.strip()
    freq = {}
    for c in word:
        if c not in freq:
            freq[c] = 0
        freq[c] = freq[c] + 1
    return freq


def part1(inp):
    count2 = 0
    count3 = 0
    has2 = False
    has3 = False
    for word in inp:
        freq = word_freq(word)
        #print(repr(freq))
        has2 = False
        has3 = False
        for f in freq:
            if freq[f] == 2 and not has2:
                count2 += 1
                has2 = True
            elif freq[f] == 3 and not has3:
                count3 += 1
                has3 = True

    return count2*count3

def compare_words(w1, w2):
    diff = 0
    reduced = []
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
        else:
            reduced.append(w1[i])
    return diff, "".join(reduced)

    
def part2(inp):
    
    for w1 in inp:
        for w2 in inp:
            c = compare_words(w1, w2) 
            if c[0] == 1:
                return c[1]
    
test = ["abcdef ","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
print(part1(test))
print(part1(inp))

print(part2(inp))