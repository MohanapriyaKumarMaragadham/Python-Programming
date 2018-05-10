a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	c=[a,b]
	z=0
	for i in range(0,2):
		num=c[i]
		s=0
		for j in range(2,num):
			if num%j==0:
				continue
			else:
				s=s+1
		if s==num-2:
			z=z+1
	if z==2:
		print "yes"
	else:
		print "no"
			
				
		
