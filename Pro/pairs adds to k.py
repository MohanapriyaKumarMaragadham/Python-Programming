a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	c=raw_input().split()
	s=0
	def add():
		h=0
		for i in range(0,a):
			x=int(c[i])
			for j in range(0,a):
				if i==j:
					continue
				else:
					w=x+int(c[j])
					if w==b:
						h=h+1
		if h>0:
			print "yes"
		else:
			print "no"
	for i in range(0,len(c)):
		if c[i].isdigit():
			s=s+1
	if len(c)==a:
		if s==a:
			add()
	elif a>len(c):
		a=len(c)
		if s==a:
			add()
	else:
		add()
else:
	print "Invalid"
	
