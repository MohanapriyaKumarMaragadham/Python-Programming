a=int(raw_input())
r=0
s=0
b=a
while(b>0):
	d=b%10
	r=d*d*d
	s=s+r
	b=b/10
if s==a:
	print "yes"
else:
	print "no"
