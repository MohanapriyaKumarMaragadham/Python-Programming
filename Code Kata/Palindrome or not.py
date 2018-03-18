n=raw_input()
a=int(n)
b=a
r=0
while(a!=0):
	c=a%10
	r=(r*10)+c
	a=a/10
if(b==r):
	print "yes"
else:
	print "no"
