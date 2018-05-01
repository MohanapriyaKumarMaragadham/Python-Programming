a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	for i in range(0,a):
		f=b.count(b[i])
		if f==1:
			print b[i]
		else:
			continue
else:
	print "invalid"
