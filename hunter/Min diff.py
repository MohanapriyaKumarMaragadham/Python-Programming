a=raw_input()
a=int(a)
b=raw_input().split()
l=[]
w=0
for i in range(a):
	if int(b[i]) not in l:
		l.append(int(b[i]))
		w=w+1
k=[]
for i in range(w/2):
	f=l[i+(w/2)]-l[i]
	k.append(f)
k.sort()
print k[0]
