õhu_temp = float(input("Sisestage õhutemp: "))
if õhu_temp > 4:
    print(str("Kõik on normaalne, kena sõitu."))
if õhu_temp < 4:
    print(str("Jäätumis oht!"))
if õhu_temp <-1:
    print(str("Mõned kohad on jääs!"))