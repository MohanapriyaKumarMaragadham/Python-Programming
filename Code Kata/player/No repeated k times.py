a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
for i in range(0,len(c)):
	t=c.count(c[i])
	if t==b:
		print c[i],
		break
