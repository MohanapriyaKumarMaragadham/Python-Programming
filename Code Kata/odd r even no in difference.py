a,b=raw_input().split()
a=int(a)
b=int(b)
if a>b:
	c=a-b
if a<b:
	c=b-a
if c%2==0:
	print "even"
else:
	print "odd"
