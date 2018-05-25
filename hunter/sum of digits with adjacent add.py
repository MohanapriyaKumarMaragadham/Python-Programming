a=raw_input()
if a.isdigit():
	l=[]
	for i in range(0,len(a)):
		l.append(int(a[i]))
	s=0
	for i in range(0,len(a)):
		for j in range(0,len(l)):
			s=s+l[j]
		l.remove(l[-1])
	print s
else:
	print "Invalid"
		
