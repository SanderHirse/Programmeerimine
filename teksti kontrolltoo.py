# coding: latin-1
import os
clear = os.system('clear');
txt = raw_input('Palun sisesta tekst : ')
y = 'Esimene ülesanne!'
print y
print 'Suurtähtedena:', txt.upper()
print 'Väiketähtedena:', txt.lower()
print 'Rea keskel:', txt.center(80)
print 'Tühikud asendatud alakriipsuga:', txt.replace(' ','_')
y2 = 'Teine ülesanne!'
print y2
print "'"+ txt.capitalize()+ "' "+ str(len(txt))+ " '"+ txt.lower()+ "'"
y3 = 'Kolmas ülesanne!'
print y3
if len(txt) <= 10:
	print 'Sisestatud tekst ei ole pikem kui 10 märki'
else:
	print 'Sisestatud tekst on pikem kui kümme märki'
if txt.find(' ') != -1:
	print 'Tekst sisaldab tühikut'
else:
	print 'Tekst ei sisalda tühikut'
if txt.find('z') == -1:
	print 'Tekst ei sisalda "z"'
else:
	print 'Tekst sisaldab "z"'
if len(txt) <1:
	print 'Teksitmuutuja ei sisalda mitte midagi'
else:
	print 'Tekstimuutuja sisaldab midagi'
if txt.isupper():
	print 'AINULT suuredtähed'
elif txt.islower():
	print 'AINULT väiketähed'
if txt.isupper() and txt.islower():
	print 'Tekstis on AINULT suuredtähed kui ka AINULT väiksedtähed'
if txt.isupper() or txt.islower():
	print 'Tekstis on kas ainult suured tähed või ainult väiksed tähed'
if txt.isdigit():
	if txt.isupper():
		print 'Tekst sisaldab numbreid ja ainult suuri tähti'
	elif txt.islower():
		print 'Tekst sisaldab numbreid ja ainult väikseid tähti'
	else:
		print 'Tekst sisaldab ainult numbreid'
else:
	print 'tekstis pole numbreid'
y4 = 'Neljas ülesanne!'
print y4
x = len(txt)-1
print '{:<10}|{}|{:>10}'.format(txt.upper(),'#'*len(txt),len(txt))
y5 = 'Viies ülesanne!'
if txt.find('n') != -1:
	print 'N märk on', txt.index('n')+1, 'märk tekstis'
else:
	print '"n" ei leitud'
