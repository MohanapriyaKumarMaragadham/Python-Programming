a=raw_input().split('|')
b=a[0]
c=a[1]
d=raw_input()
l=[]
if len(b)==len(c):
	print "Impossible"
else:
	if len(b)<len(c):
		if len(b)+len(d)==len(c):
			l.append(b)
			l.append(d)
			l.append('|')
			l.append(c)
			print "".join(l)
		else:
			print "Impossible"
	else:
		if len(c)+len(d)==len(b):
			l.append(b)
			l.append('|')
			l.append(c)
			l.append(d)
			print "".join(l)
		else:
			print "Impossible"
