a,b=raw_input().split()
a=int(a)
b=int(b)
if b>a:
	print "0"
else:
	c=0
	while(a>0):
		a=a-b
		c=c+1
	print c
