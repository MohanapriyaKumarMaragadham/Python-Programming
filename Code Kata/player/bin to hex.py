a=raw_input()
if a.isdigit():
	f=int(a,2)
	print hex(f)[2:]
else:
	print "Invalid"
