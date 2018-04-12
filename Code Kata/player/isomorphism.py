a,b=raw_input().split()
c=len(a)
d=len(b)
e=[]
f=[]
if c==d:
	for i in range(0,c):
		e.append(a[i])
	h=len(list(set(e)))
	for j in range(0,d):
		f.append(b[j])
	j=len(list(set(f)))
if(j==h):
	print "yes"
else:
	print "no"
		
