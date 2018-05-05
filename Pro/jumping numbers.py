a=raw_input()
if a.isdigit():
	a=int(a)
	res=[]
	w=0
	res.append('0')
	for i in range(1,a+1):
		i=str(i)
		if len(i)==1:
			res.append(i)
		else:
			for j in range(0,len(i)-1):
				g=int(i[j+1])
				p=int(i[j])
				if abs(g-p)==1:
					res.append(i)
	print len(res)
