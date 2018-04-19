a,b=raw_input().split()
a=int(a)
b=int(b)
c,d=raw_input().split()
c=int(c)
d=int(d)
e,f=raw_input().split()
e=int(e)
f=int(f)
w=[]
h=[]
o=[]
u=[]
if a==c==e:
	print "yes"
elif b==d==f:
	print "yes"
else:
	w.append(a)
	h.append(b)
	w.append(c)
	h.append(d)
	w.append(e)
	h.append(f)
	for i in range(0,2):
		s=w[i]-w[i+1]
		q=abs(s)
		o.append(q)
	x=len(list(set(o)))
	for i in range(0,2):
		s=h[i]-h[i+1]
		q=abs(s)
		u.append(q)
	t=len(list(set(u)))
	if x==t:
		print "yes"
	else:
		print "no"
