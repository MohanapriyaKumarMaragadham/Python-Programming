n=raw_input()
r=0
if n.isdigit():
	a=int(n)
	if a==2:
		print "yes"
	else:
		for i in (2,a):
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
