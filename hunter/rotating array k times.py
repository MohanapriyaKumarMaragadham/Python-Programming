a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	l=[]
	w=0
	def rotate(l,b):
		return l[b:]+l[:b]
	c=raw_input().split()
	for i in range(0,a):
		if c[i].isdigit():
			l.append(c[i])
		else:
			w=w+1
	if w==0:
		g=rotate(l,b)
		for i in range(0,a):
			print int(g[i]),
	elif w>0:
		print "invalid"
else:
	print "Invalid"
