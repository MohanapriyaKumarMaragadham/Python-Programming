a=raw_input()
a=int(a)
b=raw_input().split()
b.append('0')
s=0
l=[]
for i in range(len(b)-1):
	if int(b[i+1])>int(b[i]):
		s=s+1
	else:
		l.append(s)
		s=0
print max(l)+1
