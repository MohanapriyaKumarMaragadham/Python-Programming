a=int(raw_input())
b=raw_input().split()
d=len(b)
for i in range(0,d):
	z=b.count(b[i])
	if (z<2):
		print b[i]
