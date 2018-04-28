a=int(raw_input())
b=raw_input().split()
c=raw_input().split()
z=[]
for i in range(0,a):
	if b[i] in c:
		z.append(b[i])
h=list(set(z))
for i in range(0,len(h)):
	print h[i],
