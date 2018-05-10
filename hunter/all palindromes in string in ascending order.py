a=raw_input()
l=[]
m=[]
for i in range(0,len(a)):
	for j in range(0,len(a)):
		z=a[i:j+1]
		y=z[::-1]
		if z==y:
			l.append(z)
for i in l:
	if len(i)>1:
		m.append(i)
m.sort(key=len)
for i in m:
	print i
