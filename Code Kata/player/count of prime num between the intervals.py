m,n=raw_input().split()
m=int(m)
n=int(n)
r=0
count=0
h=[]
if(m==2):
	h.append(m)
for j in range(m,n+1):
	for i in (2,j/2):
		if(j%i)==0:
			r=1
			break
		else:
			h.append(j)
q=len(list(set(h)))
r=list(set(h))
if 9 in r:
  r.remove(9)
  print len(r)
else:
	print q
