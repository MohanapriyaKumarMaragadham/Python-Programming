a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
c=raw_input().split()
for i in c:
	if int(i) <b:
		l.append(int(i))
l.sort()
for i in range(0,len(l)):
	print l[i],
	
