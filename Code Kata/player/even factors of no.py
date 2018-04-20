a=int(raw_input())
for i in range(1,a+1):
	if a%i==0:
		d=i
		if d%2==0:
			print d,
