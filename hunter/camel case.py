a=raw_input().split()
l=0
for i in range(len(a)):
	g=a[i]
	if g[0].isupper() and g[1:].islower():
		l=l+1
if l==len(a):
	print "yes"
else:
	print "no"
