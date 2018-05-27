a=raw_input()
b=len(a)
l=[]
for i in range(0,b):
	l.append(a[i])
z=ord(l[0])
k=[]
for i in range(0,b):
	if z<ord(l[i]):
		y=i
for i in range(0,b):
	if i>=y:
		k.append(l[i])
print "".join(k)
