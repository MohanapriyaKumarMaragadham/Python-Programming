a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	for i in range(0,a):
		if b[i].isdigit():
			f=b.count(b[i])
			if f==1:
				print int(b[i])
			else:
				continue
		else:
			break
else:
	print "invalid"
