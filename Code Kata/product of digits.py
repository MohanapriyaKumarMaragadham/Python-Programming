a=raw_input()
d=len(a)
s=1
c=[]
for i in range(0,d):
	c.append(a[i])
for i in range(0,d):
	s=s*int(c[i])
print s
