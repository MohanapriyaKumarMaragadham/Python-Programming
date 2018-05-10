a=raw_input()
l=[]
m=[]
for i in range(0,len(a)):
	for j in range(i,len(a)):
		z=a[i:j+1]
		y=z[::-1]
		if z==y:
			l.append(z)
			m.append(len(z))
y=max(m)
for i in range(0,len(a)):
	if m[i]==y:
		print l[i]
		break
			
		
