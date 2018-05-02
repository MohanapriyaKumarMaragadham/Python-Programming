a=raw_input()
if a.isdigit():
	f=int(a,2)
	print oct(f)[1:]
else:
	print "Invalid"
