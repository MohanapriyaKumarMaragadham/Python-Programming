a=raw_input().split()
b=len(a)
minimum=int(a[0])
for i in range(1,b):
	if(minimum>int(a[i])):
		minimum=int(a[i])
print minimum
