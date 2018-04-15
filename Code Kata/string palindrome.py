a=raw_input()
c=a
b=len(a)
l=[]
for i in range(1,b):
	l.append(a[-i])
l.append(a[0])
k="".join(l)
if k==c:
	print "yes"
else:
	print "no"
