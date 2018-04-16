a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
d=raw_input().split()
count=0
for i in range(0,b):
	if d[i] in c:
		count=count+1
if count==b:
	print "YES"
else:
	print "NO"
