a=int(raw_input())
i=2
l=[]
while i<=a:
	if a%i==0:
		l.append(i)
	i=i+1
if a in l:
	l.remove(a)
if l==[]:
	print "no"
else:
	print "yes"
