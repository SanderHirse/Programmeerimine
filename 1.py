print "Tere!"

tekst = raw_input('Kirjuta number!  ');
if tekst.isdigit():
	print "Tubli " + tekst
else:
	print "Proovi uuesti!"
	uuesti = raw_input('Kirjuta palun number!  ');


print "Tere!"

rebane = raw_input('Mis häält teeb rebane? ');

print rebane.lower();

koer = raw_input('Mis häält teeb koer? ');

print koer.lower();


print "Tere!"

tekst = raw_input('Kirjuta number!  ');
if tekst.isdigit():
	print "Tubli " + tekst
else:
	print "Proovi uuesti!"
	uuesti = raw_input('Kirjuta palun number!  ');
	if uuesti.isdigit():
		print "Vapustav! " + uuesti
	else:
		print "Ei, pidid kirjutama numbri!"


print "Tere!"

nimi = raw_input('Kes sõi vanaema moosi ära? ');

print nimi.capitalize();


print "Tere!"

tekst = raw_input('Kirjuta midagi suurte tähtedega!  ');

print tekst.lower()();
