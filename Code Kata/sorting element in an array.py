a=int(raw_input())
b=raw_input().split()
z=a
while(z>0):
	largest=int(b[0])
	for i in range(1,z):
		if(largest>int(b[i])):
			largest=int(b[i])
	print largest,
	largest=str(largest)
	b.remove(largest)
	z=z-1
