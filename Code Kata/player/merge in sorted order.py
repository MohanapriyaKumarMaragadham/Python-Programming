a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
d=raw_input().split()
l=[]
for i in range(0,a):
	l.append(int(c[i]))
for i in range(0,b):
	l.append(int(d[i]))
l.sort()
for i in range(0,len(l)):
	print l[i],
