a=raw_input().split()
b=len(a)
largest_num=int(a[0])
for i in range(1,b):
	if(largest_num<int(a[i])):
		largest_num=int(a[i])
print largest_num
