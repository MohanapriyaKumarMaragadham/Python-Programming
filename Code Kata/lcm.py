x,y=raw_input().split()
x=int(x)
y=int(y)
a=[]
b=[]
c=[]
for i in range(1,x+1):
	if x%i==0:
		a.append(i)
for i in range(1,y+1):
	if y%i==0:
		b.append(i)
for i in a:
	if i in b:
		c.append(i)
k=(x*y)//max(c)
print k
