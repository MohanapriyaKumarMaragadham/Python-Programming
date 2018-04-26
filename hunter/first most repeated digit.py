a=int(raw_input())
b=raw_input().split()
k=0
for i in range(0,a):
	s=b.count(b[i])
	if s>1:
		print b[i]
		break
	else:
		k=k+1
if k==a:
	print "unique"
