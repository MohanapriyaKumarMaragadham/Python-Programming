a=int(raw_input())
b=1
s=0
r=1
print b,
print r,
for i in range(1,a-1):
	c=b+r
	print c,
	b=r
	r=c
