a=int(raw_input())
b=raw_input()
c=b.split()
min=int(c[0])
for i in range(1,a):
	if (int(c[i])<min):
		min=int(c[i])
print min
	
