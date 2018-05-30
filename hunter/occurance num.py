a,b,c=raw_input().split()
if a.isdigit() and b.isdigit() and c.isdigit():
	a=int(a)
	b=int(b)
	z=0
	for j in range(a,b):
		if c in str(j):
			z=z+1
	print z
