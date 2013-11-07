r1 = "{:^90}"
print r1.format("Arve")
print
print
r = "{:<20}{:<40}{:>5}{:>15}"
print
print r.format("Arve valjastaja", "Arve saaja", "Arve number:   ", "1234")
print r.format("Eesnimi Perenimi", "Eesnimi Perenimi", "Arve kuupaev:  ", "06.11.2013")
print r.format("Aadress", "Aadress", "Makse tahtaeg: ", "07.11.2013")
print
r2 = "{:<45}{:<20}{:<15}{:>10}"
print r2.format("Kaup", "Hind", "Kogus", "Kokku")
print r2.format("Maasikad", "10.10", "1", "10.10")
print r2.format("Mustikad", "15.00", "2", "30")
print r2.format("Pohlad", "13.30", "3", "39.90")
r3 = "{:<60}{:<15}{:>15}"
print
print r3.format(" ", "Vahesumma", "123.123")
print r3.format(" ", "Kaibemaks 20%", "2131.12")
print r3.format(" ", "Kokku", "12132.213")
print
print
print
r4 = "{:<25}{:<40}"
print r4.format("kontaktid", "Arveldus")
print r4.format("E-post: info@firma.ee", "Pank: SEB pank")
print r4.format("Telefon: 6600600", "Konto: IBAN000012341234")
