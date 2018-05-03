a=raw_input()
if len(a)<100000:
	c=['d','h','o','n','i']
	l=[]
	for i in range(0,len(a)):
		l.append(a[i])
	res=[]
	if len(l)==len(c):
		for i in l:
			if i in c:
				if i not in res:
					res.append(i)
		if len(res)==len(c):
			print "yes"
		else:
			print "no"
	else:
		print "no"
else:
	print "Invalid"
