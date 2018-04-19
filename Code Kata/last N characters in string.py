a,b=raw_input().split()
b=int(b)
c=len(a)
j=c-b
p=[]
if j==0:
	print a
else:
	for i in range(j,c):
		w=a[i]
		p.append(w)
print "".join(p)
