a,b=raw_input().split()
a=int(a)
b=int(b)
r=0
while(r<a):
	if (b**r)==a:
		print "yes"
		break
	else:
		r=r+1
if r==a:
	print "no"
