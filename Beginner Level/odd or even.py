a=raw_input()
if a.isdigit():
	a=int(a)
	if a%2==0:
		print "Even"
	else:
		print "Odd"
else:
	print "Invalid"
