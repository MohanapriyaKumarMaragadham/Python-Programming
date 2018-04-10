a=raw_input().split()
b=len(a)
largest=int(a[0])
for i in range(1,b):
	if(largest<int(a[i])):
		largest=int(a[i])
print largest
