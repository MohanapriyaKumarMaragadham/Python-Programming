a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	c=raw_input().split()
	l=[]
	k=[]
	for i in range(0,len(c)):
		if i<a:
			l.append(c[i])
		else:
			k.append(c[i])
	w=[]
	a=len(l)
	b=len(k)
	if a>b:
		e=a
	elif b>a:
		e=b
	res=[]
	for i in range(0,e):
		if l[i] in k:
			if l[i] not in res:
				w.append((l[i]))
				res.append(l[i])
	w.sort()
	for i in range(0,len(w)):
		print w[i],
else:
	print "Invalid"
