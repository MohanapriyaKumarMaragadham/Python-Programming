a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	l=[]
	y=0
	w=0
	c=raw_input().split()
	for i in range(0,a):
		if c[i].isdigit():
			l.append(int(c[i]))
		else:
			w=w+1
	for i in range(0,len(l)):
		u=l[i]
		s=0
		for j in range(0,len(l)):
			if i==j:
				break
			else:
				s=u+l[j]
				if s==b:
					y=y+1
	if w>0:
		print "invalid"
	elif y>0:
		print "YES"
	elif y==0:
		print "NO"
else:
	print "Invalid"
