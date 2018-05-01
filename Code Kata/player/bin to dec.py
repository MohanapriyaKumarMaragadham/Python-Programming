a=raw_input()
if a.isdigit():
	b=len(a)
	s=0
	l=[]
	for i in range(0,b):
		l.append(a[i])
	k=l[::-1]
	for i in range(0,b):
		s=s+(int(k[i])*(2**i))
	print s
