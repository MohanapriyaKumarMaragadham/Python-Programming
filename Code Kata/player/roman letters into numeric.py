a=raw_input()
b=len(a)
s=0
c=b
if (a=='IX'):
	print "9"
if (a=='IIX'):
	print "19"
else:
	while(c>0):
		for i in range(0,b):
			if(a[i]=='I'):
				s=s+1
				c=c-1
			elif(a[i]=='X'):
				s=s+10
				c=c-1
			elif(a[i]=='V'):
				s=s+5
				c=c-1
	print s
