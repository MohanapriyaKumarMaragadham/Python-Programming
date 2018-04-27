a=int(raw_input())
s=0
while True:
	try:
		b=raw_input().split()
		g=len(b)
		for i in range(0,g):
			s=s+int(b[i])
	except:
		break
print s
