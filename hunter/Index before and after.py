a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	s=0
	l=[]
	w=0
	for i in range(0,a):
		l.append(int(b[i]))
	for i in range(0,a-1):
		if sum(l[0:i])==sum(l[i+1:a]):
			print "yes"
			break
		else:
			w=w+1
if w==a-1:
	print "no"
