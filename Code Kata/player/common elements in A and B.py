a=int(raw_input())
b=raw_input().split()
c=raw_input().split()
z=[]
if len(b)==len(c)==a:
	for i in range(0,a):
		if c[i].isdigit() and b[i].isdigit():
			if b[i] in c:
				z.append(b[i])
		else:
			print "invalid"
			break
	h=list(set(z))
	for i in range(0,len(h)):
		print h[i],
		
