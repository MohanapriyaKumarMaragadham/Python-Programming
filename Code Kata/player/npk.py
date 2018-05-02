a,b,c=raw_input().split()
if a.isdigit() and b.isdigit() and c.isdigit():
	b=int(b)
	c=int(c)
	l=[]
	for i in range(0,len(a)):
		l.append(int(a[i]))
	for i in range(0,len(a)):
		if i==b:
			print l[i]*c
