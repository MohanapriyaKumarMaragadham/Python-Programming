a=raw_input()
b=len(a)
c=[]
e=[]
f=[]
for i in range(0,b):
	c.append(a[i])
for i in range(0,b):
	if i%2==0:
		e.append(c[i])
	else:
		f.append(c[i])
print "".join(e),
print "".join(f)
