a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
s=0
for i in range(0,a):
	if int(c[i])==b:
		print "Yes"
	else:
		s=s+1
if s==a:
	print "No"
