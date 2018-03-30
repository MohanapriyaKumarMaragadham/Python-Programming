m,n=raw_input().split()
if n.isdigit():
	if m.isdigit():
		a=int(m)
		b=int(n)
		for num in range(a+1,b):
			if num>1:
				for i in range(2,num):
					if(num%i==0):
						break
				else:
					print num
