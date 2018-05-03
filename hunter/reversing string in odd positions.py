a=raw_input().split()
l=[]
for i in range(0,len(a)):
	if i%2==0:
		p=a[i][::-1]
		l.append(p)
	else:
		l.append(a[i])
for i in range(0,len(l)):
	print l[i],
