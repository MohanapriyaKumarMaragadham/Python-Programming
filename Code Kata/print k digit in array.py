a,b=raw_input().split()
a=int(a)
b=int(b)
sum=0
count=0
c=raw_input()
d=c.split()
for digit in range(0,a):
	if digit+1 ==b:
		print d[digit]
