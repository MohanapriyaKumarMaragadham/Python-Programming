a=raw_input()
if a.isdigit():
	a=int(a)
	c=0
	while a>0:
		if a>=1000:
			a=a-1000
			c=c+1
		if a>=500 and a<1000:
			a=a-500
			c=c+1
		if a>=100 and a<500:
			a=a-100
			c=c+1
		if a>=50 and a<100:
			a=a-50
			c=c+1
		if a>=10 and a<50:
			a=a-10
			c=c+1
		if a<10:
			c=c+a
			a=a-a
	print c
else:
	print "Invalid"
		
		
