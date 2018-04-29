a,b=raw_input().split()
a=int(a)
b=int(b)
c=raw_input().split()
d=int(c[a-1])-1
c.append(str(d))
for i in range(0,a):
	if abs(int(c[i])-int(c[i+1]))==1:
		if int(c[i])==b:
			print i+1
	else:
		print "invalid sequece"
		break
	
