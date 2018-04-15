a=raw_input()
b=a.split(".")
if b[1]>'0':
	b[0]=int(b[0])+1
print b[0]
