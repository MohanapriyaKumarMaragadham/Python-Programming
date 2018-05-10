a=raw_input()
if a.isdigit():
	a=int(a)
	b=a
	for i in range(0,a):
		for j in range(0,b):
			print "1",
		b=b-1
		print 
else:
	print "Invalid"
