a=raw_input()
if a.isdigit():
	a=int(a)
	l=[]
	d=0
	for i in range(1,a):
		i=str(i)
		if len(i)==1:
			if int(i)==2:
				d=d+1
		else:
			for j in range(0,len(i)):
				if int(i[j])==2:
					d=d+1
	print d
