a=int(raw_input())
z=1
s=0
r=1
print z,
print r,
for i in range(1,a-1):
	y=z+r
	print y,
	z=r
	r=y
