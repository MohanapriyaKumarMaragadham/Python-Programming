n=raw_input()
r=0
if n.isdigit():
	a=int(n)
	if a==2:
		print "no"
	else:
		for i in (2,a):
			if(a%i)==0:
				r=1
				break
			else:
				r=0
		if(r==0):
			print "no"
		else:
			print "yes"
else:
	print "invalid"
