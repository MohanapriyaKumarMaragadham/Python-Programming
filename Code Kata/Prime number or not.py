n=raw_input()
r=0
if n.isdigit():
	a=int(n)
	for i in (2,a/2):
		if(a%i)==0:
			r=1
			break
		else:
			r=0
	if(r==0):
		print "yes"
	else:
		print "no"
else:
	print "invalid"
