a=raw_input()
if a.isdigit():
	print "Invalid"
elif ((a=='A')or (a=='a') or (a=='E') or (a=='e') or (a=='i') or (a=='I') or (a=='o') or (a=='O') or (a=='U') or (a=='u')):
	print "Vowel"
else:
	print "Consonant"
