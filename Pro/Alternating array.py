a=raw_input()
if a.isdigit():
	a=int(a)
	f=0
	b=raw_input().split()
	for i in range(len(b)-1):
		if ((int(b[i])>0 and int(b[i+1])<0) or (int(b[i])<0 and int(b[i+1])>0)):
			f=len(b)-i
			print f,
		else:
			print "1",
if f>0:
	print f-1
else:
	print "1"
