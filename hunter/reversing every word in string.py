a=raw_input().split()
f=len(a)
for i in range(0,f):
	k=a[i]
	l=[]
	for i in range(1,len(k)):
		l.append(k[-i])
	l.append(k[0])
	print "".join(l),
		
