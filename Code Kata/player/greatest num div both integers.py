n,k=raw_input().split()
n=int(n)
k=int(k)
l=[]
if n==1 or k==1:
	print "1"
else:
	for i in range(2,n*k):
		if (n%i==0 and k%i==0):
			l.append(i)
	print max(l)
