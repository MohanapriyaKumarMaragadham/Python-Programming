a=raw_input()
if a.isdigit():
	def palindrome():
		b=a[::-1]
		if a==b:
			print "yes"
		else:
			print "no"
	if(int(a)%10)==0:
		while(int(a)%10==0):
			a=int(a)
			a=a/10
		a=str(a)
		palindrome()
	else:
		palindrome()
else:
	print "Invalid"
	
