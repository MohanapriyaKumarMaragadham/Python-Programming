import re
a=raw_input()
l=[]
w=[]
def mul():
	for i in range(0,len(l)):
		u=l[i]*int(k[i])
		w.append(u)
	print "".join(w)
if len(a)<100000:
	k=re.findall("\d+",a)
	for i in range(0,len(a)):
		if a[i].isdigit():
			continue
		else:
			l.append(a[i])
	if len(l)==len(k):
		mul()
	else:
		d=len(l)-len(k)
		p=1
		for j in range(1,d+1):
			l.remove(l[-p])
		mul()
else:
	print "invalid"
		
