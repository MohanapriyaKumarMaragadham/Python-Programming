a,b=raw_input().split()
a=int(a)
b=int(b)
for i in range(a,b):
	j=i
	r=0
	s=0
	while(i>0):
		z=i%10
		r=z*z*z
		s=s+r
		i=i/10
	if s==j:
		print j
	
	
