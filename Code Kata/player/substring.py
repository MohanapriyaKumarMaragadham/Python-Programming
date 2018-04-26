a,b=raw_input().split()
l=[]
k=[]
for i in range(0,len(a)):
	l.append(a[i])
for i in range(0,len(b)):
	k.append(b[i])
count=0
for i in range(0,len(b)):
	if k[i] in l:
		count=count+1
if count==len(b):
	print "yes"
else:
	print "no"
