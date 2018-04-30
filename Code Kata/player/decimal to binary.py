a=raw_input()
if a.isdigit():
	l=[]
	w=[]
	a=int(a)
	while a>0:
		b=a%2
		l.append(str(b))
		a=a/2
	for i in range(1,len(l)):
		w.append(l[-i])
	w.append(l[0])
	print "".join(w)
else:
	print "invalid"
	
		
