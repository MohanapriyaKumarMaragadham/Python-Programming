a=raw_input()
b=raw_input()
l=[]
for i in a:
	if i in b:
		if b.index(i)==len(b)-1:
			continue
		else:
			if i not in l:
				l.append(i)
print "".join(l)
		
