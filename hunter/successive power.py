a=raw_input()
if a.isdigit():
	l=[]
	for i in range(0,len(a)):
		l.append(int(a[i]))
	if len(l)==1:
		print a
	elif len(l)==2:
		print l[0]**l[1]
	else:
		s=0
		for i in range(0,len(l)-1):
			s=s+(l[i]**l[i+1])
		s=s+(l[-1]**l[0])
		print s
else:
	print "Invalid"
