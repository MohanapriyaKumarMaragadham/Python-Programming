a,b=raw_input().split()
a=int(a)
b=int(b)
sum=0
count=0
c=raw_input()
d=c.split()
for digit in d:
	count+=1
	sum=sum+int(digit)
	if count==b:
		break
print sum
		
