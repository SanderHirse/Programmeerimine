print "Sander Hirse".center(30, "=")
import math
#
a_i = raw_input('Esimene arv: ')
b_i = raw_input('Teine arv: ')
a = float(a_i)
b = float(b_i)
#
print "Esimene ylesanne".center(30, "=")
print a, " pluss ", b, " on ", a+b
print a, " miinus ", b, " on ", a-b, " ja ", b, " miinus ", a, " on ", b-a
print a, " korda ", b, " on ", a*b
print a, " jagatud ", b, " on ", a/b, " ja ", b, " jagatud ", a, " on ", b/a
print a, " astmes ", b, " on ", a**b, " ja ", b, " astmes ", a, " on ", b**a
#
print "Teine ylesanne".center(30, "=")
print a, " radiaanides on ", math.radians(a)
print a, " kraadides on ", math.degrees(a)
print a, " siinus on ", math.sin(a)
print b, " arcus tangens on ", math.atan(b)
print "pii on ", math.pi
#
e = math.e
print "Kolmas ylesanne".center(30, "=")
tanh = ((e**a)-(e**(-a)))/((e**a)+(e**(-a)))
print a, " hyperpoolne tangens on ", tanh
x = a
snd = ((1/math.sqrt(2*math.pi))*(e**-math.sqrt(x**2)))
print "Standard normal disribution on ", snd
#
an = int(a)
bn = int(b)
print "Neljas ylesanne".center(30, "=")
print "{:04d}, {:04d}".format(an, bn)
print "{:.3f}, {:.3f}".format(an, bn)
#
print "Viies ylesanne".center(30, "=")
print "koma arvu ", a, " ymardamine ylespoole tulemuseks on", math.ceil(a)
print "koma arvu ", b, " ymardamine allapoole tulemuseks on", math.floor(b)
#
print "Sander Hirse".center(30, "=")
