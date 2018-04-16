z=['K','a','b','a','l','i']
a=int(raw_input())
c=[]
count=0
for i in range(0,a):
	b=raw_input()
	c.append(b)
for i in range(0,a):
	g=len(c[i])
	w=c[i]
	f=1
	for j in range(0,g):
		if w[j] in z:
			f=f+1
	if f==len(z):
		count=count+1
print count
