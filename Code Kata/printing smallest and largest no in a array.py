a=int(raw_input())
b=raw_input()
c=b.split()
max=int(c[0])
for i in range(1,a):
	if (int(c[i])<max):
		max=int(c[i])
print max,
for i in range(1,a):
	if (int(c[i])>max):
		max=int(c[i])
print max
