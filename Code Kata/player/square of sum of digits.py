a=raw_input()
if a.isdigit():
	b=len(a)
	s=0
	for i in range(b):
		b=int(a[i])**2
		s=s+b
	print s
else:
	print "Invalid"
