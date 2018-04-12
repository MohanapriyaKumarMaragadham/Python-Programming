a,b=raw_input().split()
c=len(a)
d=len(b)
count=0
if(c==d):
	for i in range(0,c):
		z=a[i]
		y=b[i]
		if(z==y):
			count=0
		else:
			count=count+1
if(count==1):
	print "yes"
else:
	print "no"
