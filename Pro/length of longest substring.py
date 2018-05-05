a=raw_input()
b=len(a)
res=[]
l=[]
for i in range(0,b):
	l.append(a[i])
for i in l:
	if i in res:
		break
	if i not in res:
		res.append(i)
print len(res)
