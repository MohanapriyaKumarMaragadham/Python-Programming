m=raw_input()
r=0
if m.isdigit():
	a=int(m)
	if a==2:
		print "no"
	else:
		for k in (2,a):
			if(a%k)==0:
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
