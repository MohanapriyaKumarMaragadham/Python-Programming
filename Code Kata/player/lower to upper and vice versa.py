a=raw_input()
b=len(a)
l=[]
for i in range(0,b):
	if a[i].islower():
		r=a[i].upper()
		l.append(r)
	elif a[i].isupper():
		r=a[i].lower()
		l.append(r)
print "".join(l)
	
