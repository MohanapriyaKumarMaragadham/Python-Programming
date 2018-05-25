a=raw_input()
if a.isdigit():
	l=[]
	for i in range(0,len(a)):
		l.append(int(a[i]))
	g=l[-1]
	s=0
	for i in range(0,len(l)):
		s=s+(l[i]**g)
	print s
else:
	print "Invalid"
