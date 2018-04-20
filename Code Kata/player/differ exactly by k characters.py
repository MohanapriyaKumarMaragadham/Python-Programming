a,b,c=raw_input().split()
c=int(c)
z=len(a)
y=len(b)
count=0
if z==y:
	for i in range(0,z):
		if a[i]!=b[i]:
			count=count+1
	if count==c:
		print "yes"
	else:
		print "no"
else:
	print "Invalid"
