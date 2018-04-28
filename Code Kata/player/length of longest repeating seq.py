a=int(raw_input())
b=raw_input().split()
l=[]
if len(b)==a:
	for i in range(0,a):
		t=b.count(b[i])
		l.append(t)
y=max(l)
print y
