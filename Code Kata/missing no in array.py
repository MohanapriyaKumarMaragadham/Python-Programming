a=int(raw_input())
b=raw_input().split()
s=len(b)
for i in range(1,s+1):
	w=int(b[i-1])
	if i==w:
		continue
	else:
		print i
