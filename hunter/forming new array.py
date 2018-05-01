a=raw_input()
if a.isdigit():
	h=0
	a=int(a)
	if a<=100000:
		b=raw_input().split()
		c=raw_input().split()
		l=[]
		for i in range(0,a):
			if b[i].lstrip('-').isdigit() and c[i].lstrip('-').isdigit():
				u=int(b[i])+int(c[i])
				l.append(u)
			else:
				h=h+1
		if h>0:
			print "Operation not possible"
		elif h==0:
			for j in range(0,len(l)):
				print l[j],
	else:
		print "Out of range"
else:
	print "invalid"
			
