a,b=raw_input().split()
a=int(a)
b=int(b)
k=1
l=[]
h=[]
count=0
for i in range(a,b+1):
	l.append(i)
for i in range(a,b+1):
	w=k**2
	k=k+1
	h.append(w)
for i in range(0,b-a+1):
	if l[i] in h:
		count=count+1
print count
