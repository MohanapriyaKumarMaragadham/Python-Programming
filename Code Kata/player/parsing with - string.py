a=raw_input()
l=[]
for i in range(1,len(a)):
	l.append(a[-i])
	l.append("-")
l.append(a[0])
print "".join(l)
