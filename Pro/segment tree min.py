a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	w=0
	c=raw_input().split()
	for i in range(0,len(c)):
		if c[i].isdigit():
			w=w+1
	if w==len(c):
		l=[]
		g=[]
		for i in range(0,b):
			p=raw_input().split()
			l.append(p)
		for i in range(0,len(l)):
			r=l[i]
			s=0
			if r[0].isdigit() and r[1].isdigit():
				for i in range(int(r[0])-1,int(r[1])):
					g.append(int(c[i]))
				print max(g)
				g=[]
			else:
				continue
	else:
		print "invalid"
else:
	print "Invalid"
