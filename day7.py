

def tls_allowed(seq):
	#print("Checking %r" %seq)
	i=0
	is_hypernet = False
	has_abba = False
	while i<=len(seq)-4:
		sub = seq[i:i+4]
		#print("Sub %r" % sub)
		if "[" in sub:

			i = seq.find("[", i)+1
			is_hypernet = True
		elif "]" in sub:
			i = seq.find("]", i)+1
			is_hypernet = False
		else:
			i += 1
		if len(sub) == 4 and sub[0] == sub[3] and sub[1] == sub[2] and sub[0] != sub[1]:
			if is_hypernet:
				return False
			else:
				if not has_abba:
					has_abba = True

		
	return has_abba

def ssl_allowed(seq):
	#print("Checking %r" %seq)

	is_hypernet = False
	bab_candidates = []
	#search ABA
	i=0
	while i<=len(seq)-3:
		sub = seq[i:i+3]
		#print("Sub %r" % sub)
		if "[" in sub:

			i = seq.find("[", i)+1
			is_hypernet = True
		elif "]" in sub:
			i = seq.find("]", i)+1
			is_hypernet = False
		else:
			i += 1
		if len(sub) == 3 and sub[0] == sub[2] and sub[0] != sub[1]:
			if is_hypernet:
				continue
			else:
				bab_candidates.append("%s%s%s" % (sub[1], sub[0], sub[1]))
	#print("candidates %r" % bab_candidates)
	# search for BABs in hypernet
	i = 0
	while i<=len(seq)-3:
		sub = seq[i:i+3]
		#print("Sub %r" % sub)
		if "[" in sub:

			i = seq.find("[", i)+1
			is_hypernet = True
		elif "]" in sub:
			i = seq.find("]", i)+1
			is_hypernet = False
		else:
			i += 1
		if len(sub) == 3 and sub[0] == sub[2] and sub[0] != sub[1]:
			if is_hypernet and sub in bab_candidates:
				return True
	return False
		
test = False
if test == True:
	print("TLS:")
	print(tls_allowed("abba[mnop]qrst"))
	print(tls_allowed("abcd[bddb]xyyx"))
	print(tls_allowed("aaaa[qwer]tyui"))
	print(tls_allowed("ioxxoj[asdfgh]zxcvbn"))
	print("SSL:")
	print(ssl_allowed("aba[bab]xyz"))	
	print(ssl_allowed("xyx[xyx]xyx"))
	print(ssl_allowed("aaa[kek]eke"))
	print(ssl_allowed("zazbz[bzb]cdb"))


if test == False:
	r = open("day7/input.txt", "r")		

	tls_count = 0
	ssl_count = 0
	for line in r.readlines():
		if tls_allowed(line):
			tls_count += 1
		if ssl_allowed(line):
			ssl_count += 1
		
	print("Total TLS: %r" % tls_count)
	print("Total SSL: %r" % ssl_count)
