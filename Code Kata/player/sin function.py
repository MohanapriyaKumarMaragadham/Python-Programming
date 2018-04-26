import math
a=int(raw_input())
if a<360:
	t=math.sin(math.radians(a))
	print t
elif a==360:
	a=0
	t=math.sin(math.radians(a))
	print t
	
else:
	while(a>=360):
		a=a-360
	t=math.sin(math.radians(a))
	print t
