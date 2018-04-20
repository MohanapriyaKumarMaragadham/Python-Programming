a=int(raw_input())
k=0
s=0
while(k<a):
	k=k+1
	if (k**2)==a:
		print "yes"
	else:
		s=s+1
if s==k:
	print "no"
