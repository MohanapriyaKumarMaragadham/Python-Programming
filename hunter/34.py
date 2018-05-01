a=raw_input()
b=[]
l=[]
for i in range(0,len(a)):
	b.append(a[i])
res=[]
for i in b:
	if i not in res:
		res.append(i)
print "".join(res)
