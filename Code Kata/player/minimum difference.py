a=int(raw_input())
b=raw_input().split()
b.sort()
l=[]
for i in range(0,a-1):
	d=int(b[i+1])-int(b[i])
	if d>0:
		l.append(d)
print min(l)
