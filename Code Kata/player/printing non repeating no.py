a=int(raw_input())
b=raw_input().split()
c=len(b)
for i in range(0,c):
	d=b.count(b[i])
	if d==1:
		print b[i]
