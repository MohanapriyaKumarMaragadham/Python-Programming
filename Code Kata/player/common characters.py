a,b=raw_input().split()
s=0
for i in range(0,len(a)):
	if a[i] in b:
		print "yes"
		break
	else:
		s=s+1
if s==len(a):
	print "no"
