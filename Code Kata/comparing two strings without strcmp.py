a,b=raw_input().split()
c=len(a)
d=len(b)
i=0
count=0
while(c>0):
	if(a[i]>b[i]):
		print a
		break
	elif (b[i]>a[i]):
		print b
		break
	else:
		count=count+1
		if(count==c):
			print a
			break
		else:
			continue
			

	c=c-1
	i=i+1
