a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	c=raw_input()
	z=0
	for i in range(a):
		if c in b[i]:
			z=z+1
	print z
