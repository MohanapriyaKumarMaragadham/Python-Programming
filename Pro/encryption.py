a=raw_input()
b=raw_input()
s=0
n=96
m=64
u=0
if len(a)==len(b):
	l=[]
	for i in range(0,len(a)):
		if a[i].isdigit() or b[i].isdigit():
			s=s+1
	if s==0:
		for i in range(0,len(a)):
			h=ord(a[i])
			r=ord(b[i])
			if h>96 and h<123:
				h=26+h-122
			else:
				u=u+1
				if h>64 and h<92:
					h=27+h-91
			if r>96 and r<123:
				r=26+r-122
			else:
				u=u+1
				if r>64 and r<92:
					r=27+r-91
			p=r+h
			if p>26:
				p=p-26
			if u==0:
				p=n+p
				l.append(chr(p))
			elif u>0:
				p=m+p
				l.append(chr(p))
		print "".join(l)
	else:
		print "Invalid"
else:
	print "Invalid"
