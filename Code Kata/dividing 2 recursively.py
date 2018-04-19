while True:
	try:
		a=int(raw_input())
		while(a%2 == 0):
			a=a/2
		print a
	except:
		break
