a=int(raw_input())
b=raw_input().split()
l=[]
for j in range(0,len(b)):
	smallest=int(b[0])
	for i in range(0,len(b)):
		if smallest > int(b[i]):
			smallest=int(b[i])
	l.append(smallest)
	b.remove(str(smallest))
print l[1]
