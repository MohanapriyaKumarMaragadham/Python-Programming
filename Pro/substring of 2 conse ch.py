a=raw_input().split()
b=a[0]
c=a[1]
l=0
for i in range(0,len(b)):
	for j in range(i+1,len(b)):
		g=b[i:j]
		if g in c:
			if len(g)>1:
				l=l+1
if l>0:
	print "yes"
else:
	print "no"
