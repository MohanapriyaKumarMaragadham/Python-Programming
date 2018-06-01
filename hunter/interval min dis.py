a=int(raw_input())
b=raw_input().split()
c,d=raw_input().split()
z=0
for i in range(a):
	if c==b[i]:
		ini=c
		fin=d
		break
	elif d==b[i]:
		ini=d
		fin=c
		break
for i in range(0,a):
	if b[i]==ini:
		r=i
		break
for i in range(0,a):
	if b[i]==fin:
		e=i
		break
print e-r
