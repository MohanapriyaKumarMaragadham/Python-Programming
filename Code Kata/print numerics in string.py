a=raw_input()
d=len(a)
c=[]
o=[]
for i in range(0,d):
	c.append(a[i])
for i in range(0,d):
	if c[i].isdigit():
		o.append(c[i])
print "".join(o)
