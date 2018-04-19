a,n=raw_input().split()
a=int(a)
n=int(n)
b=raw_input().split()
z=a
m=[]
while(z>0):
	largest=int(b[0])
	for i in range(1,z):
		if(largest>int(b[i])):
			largest=int(b[i])
	m.append(largest)
	largest=str(largest)
	b.remove(largest)
	z=z-1
print m[n-1]
