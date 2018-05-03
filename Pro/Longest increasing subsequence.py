a=raw_input()
if a.isdigit():
	a=int(a)
	l=[]
	s=0
	b=raw_input().split()
	for i in range(0,a):
		if b[i].isdigit():
			s=s+1
	def add():
		if s==a:
			p=0
			w=[]
			for i in range(0,a-1):
				if int(b[i+1])>=int(b[i]):
					p=p+1
				else:
					w.append(p)
					p=0
			w.append(p)
			print max(w)+1
	if len(b)==a:
		add()
	elif a>len(b):
		a=len(b)
		add()
	else:
		add()
else:
	print "Invalid"

		
			
