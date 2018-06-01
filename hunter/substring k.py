a,b=raw_input().split()
b=int(b)
for i in range(0,len(a)):
	z=a[i:b+i]
	if len(z)==b:
		print z,
