a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
i=1
while b>=1:
	w=c[-i]
	c.remove(str(w))
	b=b-1
for i in range(0,len(c)):
	print c[i],
