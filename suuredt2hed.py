t = raw_input('Sisesta tekst! ')
if t != t.upper() and 1 == t.isalpha():
	print "V2iket2hed, numbriteta"
elif t != t.upper() and 0 == t.isalpha():
	print "V2iket2hed, numbrid"
else:
	print "suuredt2hed"

