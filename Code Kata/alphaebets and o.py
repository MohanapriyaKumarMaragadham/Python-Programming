a=raw_input().split(".")
d=len(a)
count=0
count1=0
for i in range(0,d):
	z=a[i]
	x=len(z)
	for j in range(0,x):
		if z[j].isdigit():
			count=count+1
			break
		
		else:
			count1=count1+1
if(count>=1):
	print "Yes"
else:
	print "No"
