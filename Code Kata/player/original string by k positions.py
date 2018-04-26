a,b=raw_input().split()
b=int(b)
l=[]
if b<=len(a):
	for i in range(0,len(a)):
		l.append(a[i])
	k=[]
	for i in range(1,b+1):
		k.append(a[-i])
	q=len(k)
	w=[]
	while q>0:
		w.append(k[q-1])
		q=q-1
	x="".join(w)
	j=[]
	for i in range(0,len(a)-b):
		j.append(a[i])
	y="".join(j)
	u=[x,y]
	print "".join(u)
else:
	print a
	
		
