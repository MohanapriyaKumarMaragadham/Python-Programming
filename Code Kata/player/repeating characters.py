a=raw_input()
s=0
for i in range(0,len(a)):
	d=a.count(a[i])
	if d>1:
		print "yes"
		break
	else:
		s=s+1
if s==len(a):
	print "no"
