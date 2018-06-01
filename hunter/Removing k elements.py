a,b=raw_input().split()
a=int(a)
c=raw_input().split()
l=[]
for i in range(a):
	if c[i]==b:
		continue
	else:
		l.append(c[i])
if len(l)==0:
	print "empty"
else:
	for i in range(len(l)):
		print l[i],
