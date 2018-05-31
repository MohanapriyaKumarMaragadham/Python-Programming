a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
s='R'
y='G'
for i in range(0,a):
	c=raw_input()
	l.append(c)
k=[]
sum=0
for i in range(0,a):
	t=l[i]
	for j in range(0,b):
		k.append(t[j])
	for j in range(0,b-1):
		if k[j]==k[j+1]:
			if k[j]==s:
				k[j]=y
				sum=sum+5
			else:
				k[j]=s
				sum=sum+3
	k=[]
print sum
