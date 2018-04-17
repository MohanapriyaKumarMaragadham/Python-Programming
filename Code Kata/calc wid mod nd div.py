while True:
	try:
		a=raw_input().split()
		opr=[ '%', '/']
		for i in range(0,len(a)-1):
			if opr[i] in a:
				if opr[i]== '%':
					a[0]=int(a[0])
					a[2]=int(a[2])
					w=a[0]%a[2]
				elif opr[i]== '/':
					a[0]=int(a[0])
					a[2]=int(a[2])
					w=a[0]/a[2]
		print w
	except:
		break
		
