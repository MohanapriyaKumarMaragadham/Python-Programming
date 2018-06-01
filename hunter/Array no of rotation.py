a=int(raw_input())
b=raw_input().split()
c=raw_input().split()
z=0
for i in range(a):
	if b==c:
		print z
		break
	else:
		p=b[1:a]
		p.append(b[0])
		b=p
		z=z+1
