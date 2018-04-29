a,b=raw_input().split()
a=int(a)
b=int(b)
b=a-b
l=[a,b]
k=[]
for i in range(0,len(l)):
	w=l[i]
	s=1
	for i in range(0,l[i]):
		s=s*w
		w=w-1
	k.append(s)
print k[0]/k[1]
		
	
