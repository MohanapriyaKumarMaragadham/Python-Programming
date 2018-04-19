a=raw_input()
v=len(a)
count=0
for i in range(0,v):
	if a[i].isdigit():
		count=count+1
if count==v:
	print "yes"
else:
	print "no"
