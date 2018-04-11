a=raw_input()
d=len(a)
count=0
for i in range(0,d):
	if(a[i]=='0'):
		count=count+1
	elif(a[i]=='1'):
		count=count+1
if count==d:
	print "yes"
else:
	print "no"
