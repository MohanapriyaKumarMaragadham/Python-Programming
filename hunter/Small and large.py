a=raw_input()
if a.isdigit():
	a=int(a)
	b=raw_input().split()
	min=int(b[0])
	for i in range(a):
		if min>int(b[i]):
			min=int(b[i])
	f=min
	max=int(b[0])
	for i in range(a):
		if max<int(b[i]):
			max=int(b[i])
	g=max
	for i in range(a):
		if int(b[i])==int(f):
			l=i
		elif int(b[i])==int(g):
			t=i
print l+1,
print t+1
