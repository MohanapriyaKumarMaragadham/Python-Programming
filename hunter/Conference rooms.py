a,b=raw_input().split()
a=int(a)
b=int(b)
z=0
c=raw_input().split()
for i in range(a):
	if int(c[i])<=b:
		z=z+1
print z
