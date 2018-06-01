a=raw_input().split('#')
b=raw_input().split('#')
s=0
s1=0
for i in range(1,len(a)):
	s=s+int(a[i])
	s1=s1+int(b[i])
if s>s1:
	print a[0]
else:
	print b[0]
