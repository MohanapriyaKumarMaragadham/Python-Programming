a=raw_input()
if a.isdigit():
	a=int(a)
	n=2
	while 3*(n-1)<a:
		n=n*2
	print (3*(n-1))-a+1
else:
	print "Invalid"
