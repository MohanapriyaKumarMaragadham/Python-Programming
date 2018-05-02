a=raw_input()
if a.isdigit():
	l=[]
	for i in range(0,len(a)):
		l.append(a[i])
	print int(l[0])+int(l[-1])
else:
	print "Invalid"
