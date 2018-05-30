a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	if len(b)==a or len(b)>a:
		l=[]
		for j in range(a):
			l.append(1)
		for i in range(0,a-1):
			if int(b[i+1])>int(b[i]):
				if l[i+1]<=l[i]:
					l[i+1]=l[i+1]+l[i]
			elif int(b[i])>int(b[i+1]):
				if l[i]<=l[i+1]:
					l[i]=l[i]+l[i+1]
		print sum(l)
