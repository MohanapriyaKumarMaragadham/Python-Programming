a=raw_input().split()
res=[]
for i in a:
	for j in range(0,len(i)):
		if i[j].isdigit():
			continue
		else:
			t=i[j].lower()
			if t not in res:
				y=ord(t)
				if (y>96 and y<123):
					res.append(t)
g=list(set(res))
if len(g)==26:
	print "yes"
else:
	print "no"
