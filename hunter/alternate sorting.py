a=raw_input()
if a.isdigit():
	a=int(a)
	l=[]
	s=0
	b=raw_input().split()
	for i in range(0,a):
		if b[i].lstrip('-').isdigit():
			s=s+1
	if s==a:
		z=a
		while(z>0):
			largest=int(b[0])
			for i in range(1,z):
				if(largest<int(b[i])):
					largest=int(b[i])
	  		l.append(largest)
			largest=str(largest)
			b.remove(largest)
			z=z-1
		print l[0],
		if a%2==0:
			for i in range(1,a/2):
				print l[-i],
				print l[i],
			print l[a/2]
		else:
	  		for i in range(1,a/2+1):
				print l[-i],
				print l[i],
	else:
		print "Invalid"
else:
	print "Invalid"
