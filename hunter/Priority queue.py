a=raw_input()
a=int(a)
b=raw_input().split()
print int(b[0]),
for i in range(a-1):
	if int(b[i])<int(b[i+1]):
		print int(b[i]),
		b[i+1]=b[i]
	else:
		print int(b[i+1]),
