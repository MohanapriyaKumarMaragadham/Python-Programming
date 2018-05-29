a=raw_input()
if a.isdigit():
	a=int(a)
	k=0
	for i in range(0,a):
		if 2**i==a:
			print "YES"
			break
		else:
			k=k+1
if k==a:
	print "NO"
