a=int(raw_input())
c=[]
for i in range(0,a):
	b=raw_input()
	c.append(b)
o=len(c)
l=[]
e=[]
for i in range(0,o-1):
	s=c[i]
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
			l.append(s[j])
	r="".join(l)
	e.append(r)
	l=[]
s=list(set(e))
d=len(s)
for i in range(0,d):
	w=s[i]
	print w

	
	
	
	
