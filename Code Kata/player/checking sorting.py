a=int(raw_input())
b=raw_input().split()
count=0
g=a
i=0
s=0
while (a>1):
	if int(b[i])<=int(b[i+1]):
		count=count+1
		i=i+1
		a=a-1
	else:
		s=s+1
		i=i+1
		a=a-1
if count==g-1:
	print "yes"
else:
	print "no"
