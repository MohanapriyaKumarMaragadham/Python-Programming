n,a,d=raw_input().split()
n=int(n)
a=int(a)
d=int(d)
s=0
r=0
while(n>0):
	s=s+a
	a=a+d
	n=n-1
print s
