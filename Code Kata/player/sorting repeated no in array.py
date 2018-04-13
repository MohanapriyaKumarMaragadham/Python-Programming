a=int(raw_input())
b=raw_input().split()
s=[]
count=0
for i in range(0,a):
	u=b.count(b[i])
	if(u>1):
		s.append(b[i])
	else:
		count=count+1
k=list(set(s))		
d=len(k)
if(count==a):
	print "unique"
else:
	l=[]
	for j in range(0,d):
		largest=int(k[0])
		g=len(k)
		for i in range(1,g):
			if(largest>int(k[i])):
				largest=int(k[i])
		l.append(largest)
		k.remove(str(largest))
	for i in l:
		print i,



