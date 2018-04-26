a=int(raw_input())
l=[]
for i in range(1,a):
	if a%i==0:
		d=i
		if d%2!=0:
			l.append(d)
t=max(l)
if t==1:
	print a
else:
	l.remove(1)
	for i in range(0,len(l)):
		print l[i],
