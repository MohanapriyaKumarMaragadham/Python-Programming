a=raw_input()
b=len(a)
c=0
s=0
for i in range(0,b):
	if ((a[i]=='A')or (a[i]=='a') or (a[i]=='E') or (a[i]=='e') or (a[i]=='i') or (a[i]=='I') or (a[i]=='o') or (a[i]=='O') or (a[i]=='U') or (a[i]=='u')):
		c=c+1
	else:
		s=s+1
if c>0:
	print "yes"
else:
	print "no"
