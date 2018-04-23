a=raw_input()
b=len(a)
l=[]
m=[]
for i in range(0,b):
	l.append(a[i])
m.append(l[0]),
o=1
for i in range(0,b/3):
	k=o*3
	if k<b:
		m.append(l[k]),
		o=o+1
print "".join(m)
