a=raw_input()
if '@' in a:
	if a.count('@') and a.count('.') ==1:
		t=a.index('@')
		s=a.index('.')
		if len(a[t+1:s])==5:
			if len(a[:t])>=3:
				if '.com' in a:
					print "YES"
				else:
					print "NO"
			else:
				print "NO"
		else:
			print "NO"
	else:
		print "NO"
else:
	print "NO"
