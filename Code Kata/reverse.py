a=raw_input()
s=len(a)
l=[]
f=[]
for i in range(0,s):
	l.append(a[i])
for i in range(1,s):
	f.append(l[-i])
f.append(l[0])
print "".join(f)
