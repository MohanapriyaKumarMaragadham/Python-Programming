a1=raw_input()
b1=[]
l=[]
for i in range(0,len(a1)):
	b1.append(a1[i])
res1=[]
for i in b1:
	if i not in res1:
		res1.append(i)
print "".join(res1)
