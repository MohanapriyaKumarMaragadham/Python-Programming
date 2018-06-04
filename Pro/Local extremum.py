a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	l=[]
	for i in range(len(b)):
		if i==0:
			lmin=int(b[i])
		elif i==len(b)-1:
			lmax=int(b[i])
		else:
			if ((int(b[i-1])>int(b[i]) and int(b[i])<int(b[i+1])) or (int(b[i-1])<int(b[i]) and int(b[i])>int(b[i+1]))):
				l.append(b[i])
	print len(l)
