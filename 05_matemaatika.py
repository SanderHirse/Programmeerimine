import math
text = "SUPER vinge Kahekymmneesimese sajandi siinuste arvutaja"
print "", text.center(75, "=")
num = raw_input("Keeruta yks numbe, jouuuu! ")
nump = float(num)
print "Tangents: ",math.tan(nump * math.pi/180)
print "Cossiinus: ",math.cos(nump * math.pi/180)
print "Siinus: ",math.sin(nump * math.pi/180)
print ""
text = "Risttahukas"
print "", text.center(75, "=")
#risttahukas
R = "Sisestage andmed!"
print R.center(75, "=")
#andmed
r_a_inp = raw_input("Risttahuka lyhem kylg: ")
r_a = float(r_a_inp)
r_b_inp = raw_input("Risttahuka pikem kylg: ")
r_b = float(r_b_inp)
r_c_inp = raw_input("Risttahuka k6rgus: ")
r_c = float(r_c_inp)
#servade pikkus
r_servad = 4*(r_a+r_b+r_c)
print "servad = {}"\
.format(r_servad)
#pindala
r_pindala = 2*(r_a*r_b+r_b*r_c+r_a*r_c)
print "pindala = {}"\
.format(r_pindala)
#ruumala
r_ruumala = r_a*r_b*r_c
print "ruumala = {}"\
.format(r_ruumala)
