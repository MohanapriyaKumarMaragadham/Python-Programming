a=raw_input()
b=len(a)
x='('
t=')'
l=[]
p=0
w=0
if b%2==0:
	for i in range(0,b):
		if a[i]==x:
			p=p+1
		elif a[i]==t:
			w=w+1
	if w==p:
		print "yes"
	else:
		print "no"
else:
	print "no"
	
