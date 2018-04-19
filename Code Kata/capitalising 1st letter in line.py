a=raw_input().split()
z=len(a)
e=[]
for i in range(0,z):
	w=len(a[i])
	y=a[i]
	for j in range(0,w):
		if(j==0):
			s=y[j].upper()
			e.append(s)
		elif(j>0):
			e.append(y[j])
	print "".join(e),
	e=[]
