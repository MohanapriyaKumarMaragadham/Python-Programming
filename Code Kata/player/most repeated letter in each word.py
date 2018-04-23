a=raw_input().split()
y=[]
for i in range(0,len(a)):
	g=a[i]
	r=len(g)
	for j in range(0,r):
		u=g.count(g[j])
		y.append(u)
	w=max(y)
	for k in range(0,r):
		if w==y[k]:
			print g[k],
			break
	y=[]
	
		
