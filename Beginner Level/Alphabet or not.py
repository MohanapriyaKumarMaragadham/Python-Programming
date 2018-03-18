a=raw_input()
if a.isdigit():
	print "No"
elif ((a>='A'and a<='Z') or (a>='a'and a<='z')):
	print "Alphabet"
else:
	print "No"
