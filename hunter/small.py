a=raw_input()
if a.isdigit():
	a=int(a)
	l=[]
	b=raw_input().split()
	for i in range(len(b)):
		if b[i].isdigit():
			l.append(int(b[i]))
	if len(l)==a or len(l)>a:
		for i in range(a-1):
			if l[i+1]<l[i]:
				print l[i+1],
			else:
				print "-1",
		print "-1"
	else:
		print "Invalid"
