a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	l=[]
	for i in range(0,a):
		if b[i].isdigit():
			l.append(int(b[i]))
	if len(l)==len(b):
		y=max(l)
		z=min(l)
		print y-z
	else:
		print "Invalid"
else:
	print "invalid"
