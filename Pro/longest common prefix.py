a=int(raw_input())
c=[]
for i in range(0,a):
	b=raw_input()
	c.append(b)
o=len(c)
l=[]
e=[]
for i in range(0,o-1):
	s=c[0]
	f=c[i+1]
	q=len(s)
	t=len(f)
	if q>t:
		u=t
	elif q<t:
		u=q
	elif q==t:
		u=q
	for j in range(0,u):
		if(s[j]==f[j]):
			l.append(f[j])
		else:
			break
	r="".join(l)
	e.append(r)
	l=[]
h=len(e)
w=[]
v=[]
if h==1:
	print e[0]
else:
	for i in range(0,h-1):
		s=e[0]
		f=e[i+1]
		q=len(s)
		t=len(f)
		if q>t:
			u=t
		elif q<t:
			u=q
		elif q==t:
			u=q
		for j in range(0,u):
			if(s[j]==f[j]):
				w.append(f[j])
			else:
				break
		r="".join(w)
		v.append(r)
		w=[]
	print v[0]
	
	
	
	
