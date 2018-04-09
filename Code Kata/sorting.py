
a=int(raw_input())
b=raw_input().split()
z=a
c=[]
while(z>0):
	largest=int(b[0])
	for i in range(1,z):
		if(largest>int(b[i])):
			largest=int(b[i])
	largest=str(largest)
	b.remove(largest)
	z=z-1
	c.append(largest)
d=len(c)
if(d%2!=0):
	e=(d+1)/2
	print c[e-1]
