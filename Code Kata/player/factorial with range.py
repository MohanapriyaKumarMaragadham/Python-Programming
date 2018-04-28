a=raw_input()
if a.isdigit():
	a=int(a)
	if a<=25:
		b=a
		s=1
		for i in range(0,a):
			s=s*b
			b=b-1
		print s
	else:
		print "invalid(out of range)"
else:
	print "invalid"
			
