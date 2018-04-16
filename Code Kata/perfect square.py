a,b=raw_input().split()
a=int(a)
b=int(b)
c=a*b
d=0
j=2
for i in range(1,c):
	if(i**j)==c:
		d=d+1
		break
if d>0:
	print "yes"
else:
	print "no"
