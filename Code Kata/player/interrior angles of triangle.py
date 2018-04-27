a,b,c=raw_input().split()
a=int(a)
b=int(b)
c=int(c)
d=a+b+c
if a==0 or b==0 or c==0:
	print "no"
else:
	if d==180:
		print "yes"
	else:
		print "no"
