kirja_suurus = float(input("Sisesta kirja suurus(MB):"))
kirja_teema = str(input("Sisesta kirja teema, kui pole siis ära pane midagi:"))
kirjaga_fail = str(input("Kas kirjaga on kaasas ka fail? (jah) või (ei)"))
if kirjaga_fail == "jah" and kirja_suurus > 1.0 or kirja_teema == "":
    print(str("Kiri on spämm"))
else:
    print(str("Kiri ei ole spämm."))


    
