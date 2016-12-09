
def decompress(seq):
	res = []
	seq = seq.strip()
	i = 0
	while i < len(seq):
		if seq[i] != "(":
			res.append(seq[i])
			i += 1
		else:
			mark = seq.find(")", i)
			marker = seq[i+1:mark]
			m_len, m_rep = map(int, marker.split("x"))
			for j in range(m_rep):
				res.append(seq[mark+1:mark+1+m_len])
			i = mark+m_len+1
	decompressed = "".join(res).replace("\s", "")
	#print repr(decompressed)
	return len(decompressed)


def decompress_v2(seq):
	res_len = 0
	seq = seq.strip()
	#print("decompressing subseq with len %s" % len(seq))
	i = 0
	if "(" not in seq:
		return len(seq)

	while i < len(seq):
		
		if seq[i] != "(":
			res_len += 1
			i += 1
		else:
			mark = seq.find(")", i)
			marker = seq[i+1:mark]
			m_len, m_rep = map(int, marker.split("x"))
			res_len += m_rep*decompress_v2(seq[mark+1:mark+1+m_len])
			i = mark+m_len+1

	#print repr(decompressed)
	return res_len

test = False
version = 2
if version == 1:
	if test:
		print(decompress("ADVENT"))
		print(decompress("A(1x5)BC"))
		print(decompress("(3x3)XYZ"))
		print(decompress("A(2x2)BCD(2x2)EFG"))
		print(decompress("(6x1)(1x3)A"))
		print(decompress("X(8x2)(3x3)ABCY"))
	else:
		r = open("day9/input.txt", "r")
		print(decompress(r.read()))

elif version == 2:

	if test:
		print(decompress_v2("ADVENT"))
		print(decompress_v2("A(1x5)BC"))
		print(decompress_v2("(3x3)XYZ"))
		print(decompress_v2("X(8x2)(3x3)ABCY"))
		print(decompress_v2("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
		print(decompress_v2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))
	else:
		r = open("day9/input.txt", "r")
		print(decompress_v2(r.read()))
