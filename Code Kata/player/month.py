a=raw_input().split('-')
l=['January','February','March','April','May','June','July','August','September','October','November','December']
g=a[1]
if g[-2]=='0':
	k=g[-1]
else:
	k=g
if int(k)<13:
	print l[int(k)-1]
else:
	print "Invalid"
