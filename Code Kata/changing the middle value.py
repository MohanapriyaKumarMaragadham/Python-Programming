a=raw_input()
b=len(a)
k=(b+1)/2
p=[]
for i in range(0,b):
	p.append(a[i])
p.remove(a[k-1])
p.insert(k-1,'*')
print "".join(p)
