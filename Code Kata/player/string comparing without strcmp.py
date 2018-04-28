a,b=raw_input().split()
l=[]
k=[]
c=0
if len(a)==len(b):
	for i in range(0,len(a)):
		if a[i]==b[i]:
			c=c+1
	if c==len(a):
		print "yes"
	else:
		print "no"
else:
	print "no"
