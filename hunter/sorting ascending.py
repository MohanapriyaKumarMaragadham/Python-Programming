a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	def ans():
		l=[]
		for i in range(0,a):
			m=b[i].lower()
			l.append(m)
		l.sort()
		for i in range(0,a):
			print l[i]
	if a==len(b):
		ans()
	elif len(b)>a:
		ans()
	elif len(b)<a:
		a=len(b)
		ans()
