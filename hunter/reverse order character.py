a=raw_input()
res=[]
for i in a:
	if i not in res:
		res.append(i)
res.sort(reverse=True)
print "".join(res)
