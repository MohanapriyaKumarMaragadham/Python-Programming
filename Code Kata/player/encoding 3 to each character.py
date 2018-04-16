a=raw_input()
b=len(a)
l=[]
k=[]
def new():
	u=ord(l[i])
	c=chr(u)
	k.append(c)
	return k
def new1():
	u=ord(l[i])
	j=u+3
	c=chr(j)
	k.append(c)
	return k
for i in range(0,b):
	l.append(a[i])
for i in range(0,b):
	if l[i]=='Z':
		l.remove(l[i])
		l.insert(i,'C')
		new()
	elif l[i]=='z':
		l.remove(l[i])
		l.insert(i,'c')
		new()
	elif l[i]=='Y':
		l.remove(l[i])
		l.insert(i,'B')
		new()
	elif l[i]=='y':
		l.remove(l[i])
		l.insert(i,'b')
		new()
	elif l[i]=='X':
		l.remove(l[i])
		l.insert(i,'A')
		new()
	elif l[i]=='x':
		l.remove(l[i])
		l.insert(i,'a')
		new()
	else:
		new1()
		
print "".join(k)



