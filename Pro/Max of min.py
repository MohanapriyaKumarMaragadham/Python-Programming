a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
l=[]
for i in range(a):
	l.append(int(c[i]))
w=[]
k=[]
z=[]
if b>=3:
	print max(l)
elif b==1:
	print min(l)
elif b==2:
	for i in range(0,a-1):
		w.append(min(l[0:a-i-1]))
		k.append(min(l[a-i-1:a]))
	for i in range(0,a-1):
		z.append(max(w[i],k[i]))
	print max(z)
