n=raw_input()
a=int(n)
r=0
for i in (2,a/2):
	if(a%i)==0:
		r=1
		break
	else:
		r=0
if(r==0):
	print "prime"
else:
	print "not"
