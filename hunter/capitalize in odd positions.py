a=raw_input().split()
k=[]
for i in range(0,len(a)):
	g=len(a[i])
	k.append(g)
b="".join(a)
l=[]
for i in range(0,len(b)):
	if i%2==0:
		d=b[i].upper()
		l.append(d)
	else:
		l.append(b[i])
e=[]
h="".join(l)
m=0
for i in range(0,len(k)):
	print h[m:k[i]+m],
	m=k[i]+m
