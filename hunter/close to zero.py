a=int(raw_input())
b=raw_input().split()
min=9999
for i in range(0,a):
	w=int(b[i])
	for j in range(0,a):
		if i==j:
			continue
		else:
			y=w+int(b[j])
			y=abs(y)
			if min>y:
				min=y
				l=w
				k=b[j]
if l>0:
	print l,
	print k
else:
	print k,
	print l
		
