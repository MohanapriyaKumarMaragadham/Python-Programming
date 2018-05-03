a=raw_input()
if a.isdigit():
	a=int(a)
	l=[]
	w=0
	for i in range(0,a):
		b=raw_input().split()
		c=len(b)
		for j in range(0,a):
			if b[j].isdigit():
				l.append(int(b[j]))
			else:
				w=w+1
	if w==0:
		s=0.000000
		c=0.000000
		for i in range(0,len(l)):
			s=s+l[i]
			c=c+1
		avg=s/c
		print "%.6f"%avg
	else:
		print "Invalid"
else:
	print "Invalid"
