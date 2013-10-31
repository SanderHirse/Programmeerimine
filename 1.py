text = "Esimene kysimus"
print "", text.center(50, "=")

teksti = raw_input('Sisesta tyhik! ');
if teksti.isspace():
        print "Tubli "
else:
        print "Proovi uuesti!"
        uuestii = raw_input('Sisesta tyhik! ');
	if uuestii.isspace():
		print "V2ga tubli!"
	else:
		print "Tyhiks on k6ige pikem klahv sinu klaviatuuril!"

text = "Teine kysimus"
print "", text.center(50, "=")

rebane = raw_input('Mis h22lt teeb rebane? ');

print "rebane teeb " + rebane.lower();

koer = raw_input('Mis h22lt teeb koer? ');

print "Koer teeb " + koer.lower(); 

text = "Kolmas kysimus"
print "", text.center(50, "=")

tekst = raw_input('Kirjuta number! ');
if tekst.isdigit():
        print "Tubli " + tekst
else:
        print "Proovi uuesti!"
        uuesti = raw_input('Kirjuta palun number! ');
        if uuesti.isdigit():
                print "Vapustav! " + uuesti
        else:
                print "Ei, oli vaja kirjutada number !"

text = "Neljas kysimus"
print "", text.center(50, "=")

nimi = raw_input('Kes s6i vanaema moosi 2ra? ');

print "Vanaema moosi s6i 2ra" + nimi.capitalize();

text = "Viies kysimus"
print "", text.center(50, "=")

tekst = raw_input('Kirjuta midagi suurte t2htedega! ');

print tekst.lower();
