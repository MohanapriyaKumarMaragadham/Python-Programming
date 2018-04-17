a,b=raw_input().split()
a=int(a)
b=int(b)
if ((a<(2**32)) and (b<(2**32))):
	if b>a:
		print b-a
else:
	print "End of File"
