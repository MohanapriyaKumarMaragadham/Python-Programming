a=int(raw_input())
b,c=raw_input().split()
b=int(b)
c=int(c)
s=0
for i in range(b,c):
	if(i==a):
		print "yes"
	else:
		s=s+1
if s==c-b:
	print "no"
