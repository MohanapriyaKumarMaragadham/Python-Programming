a=raw_input()
d=len(a)
c=[]
for i in range(0,d):
	c.append('0')
for i in range(0,d):
	if(i%2==0):
		c[i]=a[i+1]

	else:
		c[i]=a[i-1]

k="".join(c)
print k
