nimi = str(input("Sisestage oma nimi:"))
lubatud_kiirus = int(input("Sisestage lubatud kiirus km/h:"))
tegelik_kiirus = int(input("Sisestage oma kiirus km/h:"))
oled_ületanud = tegelik_kiirus - lubatud_kiirus
arvutatud_trahv = oled_ületanud * 3
trahv = min(arvutatud_trahv, 190)
print( str(nimi) + ", kiiruse ületamise eest on sinu trahv " + str(trahv) + " eurot")