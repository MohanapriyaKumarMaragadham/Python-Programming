a=raw_input()
b=len(a)
v=[]
for i in range(0,b):
	v.append(a[i])
for i in range(0,b):
	if int(v[i])%2!=0:
		print v[i],
