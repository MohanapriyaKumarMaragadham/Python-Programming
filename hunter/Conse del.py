a=raw_input()
if a.isdigit():
	l=[]
	for i in range(len(a)):
		l.append(a[i])
	if len(list(set(l)))==len(a):
		print a
	else:
		k=[]
		for i in range(len(l)-1):
			if int(l[i+1])==int(l[i]):
				k.append(i)
		w=[]
		c=[]
		for j in range(0,len(k)):
			y=k[j]
			for i in range(0,len(l)):
				if i==y:
					continue
				else:
					w.append(l[i])
			c.append("".join(w))
			w=[]
		print max(c)
