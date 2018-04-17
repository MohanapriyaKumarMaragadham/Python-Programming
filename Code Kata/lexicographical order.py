a=raw_input()
d=len(a)
c=[]
for i in range(0,d):
	c.append(a[i])
c.sort()
print "".join(c)
