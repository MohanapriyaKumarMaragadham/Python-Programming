a=int(raw_input())
b=raw_input().split()
l=[]
k=[]
c=0
d=0
for i in range(0,a):
	if int(b[i])%2==0:
		c=c+1
		k.append(b[i])
	else:
		d=d+1
		l.append(b[i])
if c<d:
	print k[0]
else:
	print l[0]
