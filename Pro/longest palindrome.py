a=raw_input()
b=a[::-1]
if a==b:
	print "0"
else:
	s=0
	l=[]
	for i in range(0,len(a)):
		l.append(a[i])
	res=[]
	for i in l:
		if l.count(i)==1:
			res.append(i)
	print len(res)
