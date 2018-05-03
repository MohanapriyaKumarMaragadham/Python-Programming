a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	l=[]
	c=0
	dict1={}
	for i in range(0,a):
		if b[i].isdigit():
			l.append(int(b[i]))
			c=c+1
	if c==a:
		k=[]
		for i in range(0,a):
			x=bin(l[i])[2:]
			n=x.count('1')
			k.append(n)
		d = {l[x]:k[x] for x in range(a)}
		f=[i[0] for i in sorted(d.items(), key=lambda x:x[1])]
		for i in range(1,len(f)):
			print f[-i],
		print f[0]
