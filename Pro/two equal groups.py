a,b,c=raw_input().split()
if a.isdigit() and b.isdigit() and c.isdigit():
	a=int(a)
	b=int(b)
	c=int(c)
	l=a
	s=0
	d=0
	while a>0:
		p=b+c
		s=p+s
		d=p+d
		a=a-(2*p)
	if l==s+d:
		print "YES"
	else:
		print "NO"
else:
	print "Invalid"
	
		
