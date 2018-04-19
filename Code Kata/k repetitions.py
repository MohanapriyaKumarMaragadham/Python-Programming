n,k=raw_input().split()
a=raw_input().split()
n=int(n)
k=int(k)
count=0
for i in range(0,n):
	if int(a[i])==k:
		count=count+1
print count
