a,b=raw_input().split()
a=int(a)
b=int(b)
e=a/2
s=0
i=1
p=b
while i<b:
	for j in range(1,b):
		u=j*p
		if u==e:
			s=s+1
			break
	i=i+1
	p=p-1
if s>0:
	print "yes"
else:
	print "no"
		
	
	
