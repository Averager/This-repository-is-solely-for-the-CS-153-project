	if x >= 2**(len(p)-1):
		invalid = True

if invalid:
	print 'invalid input'
else:
	print
	print "1. addition"
	print "2. subtraction"
	print "3. multiplication"
	print "4. division"
	print
	i = input()

	if i == 1 or i == 2:
		c = []
		j = -1
		if len(a) >= len(b):
			while j >= -len(a):
				if j >= -len(b):
					c = [a[j] ^ b[j]] + c
				else:
					c = [a[j]] + c
				j -= 1
		elif len(b) > len(a):
			while j >= -len(b):
				if j >= -len(a):
					c = [a[j] ^ b[j]] + c
				else:
					c = [a[j]] + c
				j -= 1
		l = max(len(a),len(b))
		print " ",
		for x in range(l - len(a)):
			print " ",
		for x in a:
			print x,
		print
		if i == 1:
			print "+",
		elif i == 2:
			print "-",
		for x in range(l - len(b)):
			print " ",
		for x in b:
			print x,
		print
		print "=",
		for x in c:
			print x,
		print
		print
	elif i == 3:
		c = []
		j = -1
		k = 0
		while j >= -len(a):
			c.append([])
			n = a[j]
			for x in range(len(p)-1):
				c[k].append(n%2)
				n /= 2
			j -= 1
			k += 1
		d = []
		j = -1
		k = 0
		while j >= -len(b):
			d.append([])
			n = b[j]
			for x in range(len(p)-1):
				d[k].append(n%2)
				n /= 2
			j -= 1
			k += 1
		e = []
		for j in range(len(a)+len(b)-1):
			e.append([])
			for x in range(len(p)-1):
				e[j].append(0)

		o = max(len(a),len(b))
		print " ",
		for x in range(o - len(a)):
			print " ",
		for x in a:
			print x,
		print
		print "*",
		for x in range(o - len(b)):
			print " ",
		for x in b:
			print x,
		print
		for j in range(len(c)):
			for k in range(len(d)):
				for l in range(len(c[j])):
					for m in range(len(d[k])):
						if (l+m) >= len(p)-1:
							if c[j][l]*d[k][m] == 1:
								n = ((l+m)%(len(p)-1))+1
								o = -1
								while n < len(p):
									e[j+k][o] ^= p[n]
									n+=1
									o-=1
						else:
							e[j+k][l+m] ^= c[j][l]*d[k][m]
		f = e[::-1]
		print "=",
		for x in range(len(f)):
			n = 0
			for y in range(len(f[x])):
				if f[x][y] == 1:
					n += 2**y
			print n,
		print

	elif i == 4:
		print "div"
