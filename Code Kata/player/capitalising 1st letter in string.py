a,b=raw_input().split()
z=len(a)
y=len(b)
u=a
v=b
e=[]
f=[]
for i in range(0,z):
	if(i==0):
		s=a[i].upper()
		e.append(s)
	elif(i>0):
		e.append(a[i])
n="".join(e)
print n,
for i in range(0,y):
	if(i==0):
		s=b[i].upper()
		f.append(s)
	elif(i>0):
		f.append(b[i])
m="".join(f)
print m
