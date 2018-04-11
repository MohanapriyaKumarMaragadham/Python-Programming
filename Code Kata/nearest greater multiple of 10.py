a=int(raw_input())
if a%10==0:
	print a
else:
	while(a%10!=0):
		a=a+1
	print a
