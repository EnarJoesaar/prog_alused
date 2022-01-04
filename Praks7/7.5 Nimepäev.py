from urllib.request import urlopen
fail = str(input("Sisestage kuu: "))
site = urlopen("https://kodu.ut.ee/~eno/mooc/" + fail)
baidid = site.read()
tekst = baidid.decode()
ridadeKaupa = tekst.splitlines()
päev = int(input("Sisestage päev: "))
site.close()

i = 1
for rida in ridadeKaupa:
    if i == päev:
        nimed = rida
        break
    i += 1
print("Kuupäeval " + str(päev) + ". " + str(fail) + " on nimedepäev järgmiset inimestel: " + "\n" + nimed)