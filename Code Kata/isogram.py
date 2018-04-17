a=raw_input()
d=len(a)
c=[]
o=[]
for i in range(0,d):
	c.append(a[i])
p=list(set(c))
if len(p)==len(c):
	print "Yes"
else:
	print "No"
	
