import re
a=raw_input()
l=[]
w=[]
k=re.findall("\d+",a)
for i in range(0,len(a)):
	if a[i].isdigit():
		continue
	else:
		l.append(a[i])
if len(l)==len(k):
	for i in range(0,len(l)):
		u=l[i]*int(k[i])
		w.append(u)
	print "".join(w)
else:
	print "invalid"
