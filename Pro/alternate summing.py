a=raw_input()
if a.isdigit():
	a=int(a)
	s=0
	b=raw_input().split()
	for i in range(0,a):
		if b[i].isdigit():
			s=s+1
	if s==a:
		b.sort(reverse=True)
		sum=0
		for i in range(0,a):
			if i%2==0:
				sum=sum+int(b[i])
		print sum
	else:
		print "Invalid"
else:
	print "invalid"
			
			
