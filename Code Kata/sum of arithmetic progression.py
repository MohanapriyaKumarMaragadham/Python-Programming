a,b,c=raw_input().split()
a=int(a)
b=int(b)
c=int(c)
w=[]
s=a
sum=0
w.append(s)
for i in range(1,c):
	s=a+b
	w.append(s)
	a=s
y=len(w)
for i in range(0,y):
    sum=sum+int(w[i])
print sum
