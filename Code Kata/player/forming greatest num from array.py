a=int(raw_input())
b=raw_input().split()
l=[]
s=[]
y=len(b)
count=0
for e in range(0,y):
	if b[e]=='0':
		count=count+1
if (count ==y):
	print "0"
else:
	for j in range(0,y):
		largest=int(b[0])
		g=len(b)
		for i in range(1,g):
			if(largest<int(b[i])):
				largest=int(b[i])
		l.append(largest)
		b.remove(str(largest))
	for i in l:
		s.append(str(i))
	w="".join(s)
	print w



