a=raw_input()
if a.isdigit():
	s=0
	for i in range(0,len(a)):
		s=s+(int(a[i])**2)
	print s
