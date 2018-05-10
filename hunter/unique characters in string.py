a=raw_input()
l=[]
for i in range(0,len(a)):
	d=a.count(a[i])
	if d==1:
		l.append(a[i])
print "".join(l)
