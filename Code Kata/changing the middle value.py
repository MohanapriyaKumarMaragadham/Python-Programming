a=raw_input()
b=len(a)
k=(b+1)/2
p=[]
for i in range(0,b):
	p.append(a[i])
if(b%2!=0):
	p.remove(a[k])
	p.insert(k-1,'*')
	print "".join(p)
else:
	p.remove(a[k])
	p.insert(k,'*')
	print "".join(p)
