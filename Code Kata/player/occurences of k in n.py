a,b=raw_input().split()
b=int(b)
f=len(a)
l=[]
count=0
for i in range(0,f):
	l.append(a[i])
for i in range(0,f):
	if int(l[i])==b:
		count=count+1
print count
