a,b=raw_input().split()
a=int(a)
b=int(b)
def ans():
	i=1
	e=10**b
	while(i<a):
		d=a*i
		i=i+1
		if d%a==0:
			if d%e==0:
				print d
				break
def ans1():
	i=1
	e=10**b
	while(i<a):
		d=a*i
		i=i*10
		if d%a==0:
			if d%e==0:
				print d
				break
if b<6:
	ans()
else:
	ans1()
