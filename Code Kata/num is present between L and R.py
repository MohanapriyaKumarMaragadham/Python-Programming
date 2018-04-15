a=int(raw_input())
b,c=raw_input().split()
b=int(b)
c=int(c)
s=0
for i in range(b+1,c):
	if(i==a):
		print "yes"
		break
	else:
		s=s+1
if s==c-b-1:
	print "no"
