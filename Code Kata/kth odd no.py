n,k=raw_input().split()
a=raw_input().split()
n=int(n)
k=int(k)
p=[]
for i in range(0,n):
	if int(a[i])%2!=0:
		p.append(a[i])
print p[k-1]
