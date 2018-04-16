a=raw_input()
b=len(a)
l=[]
k=[]
for i in range(0,b):
	l.append(a[i])
for i in range(0,b):
	g=a.count(a[i])
	k.append(g)
w=max(k)
if w>1:
	for i in range(0,b):
		if w==k[i]:
			y=i
			break
	print l[y]
else:
	print "unique"
