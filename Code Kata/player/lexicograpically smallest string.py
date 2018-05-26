a=raw_input()
if a.isdigit():
	a=int(a)
	l=[]
	for i in range(0,a):
		b=raw_input()
		l.append(b)
	l.sort()
	print l[0]
		
