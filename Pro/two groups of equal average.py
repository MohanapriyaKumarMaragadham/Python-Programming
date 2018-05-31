a=raw_input()
if a.isdigit():
	a=int(a)
	s=0
	b=raw_input().split()
	l=[]
	for i in range(0,a):
		l.append(int(b[i]))
		s=s+int(b[i])
	su=0
	sum1=0
	m=0
	for i in range(0,a-1):
		avg=0
		avg1=0
		su=su+l[i]
		sum1=s-su
		avg=su/(i+1)
		avg1=sum1/(a-i-1)
		if avg==avg1:
			m=1
			print "yes"
			break
		else:
			continue
if m==0:
	print "no"
		
			
	
