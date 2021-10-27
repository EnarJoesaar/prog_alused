istekoha_valik = str(input("Kas soovite valida (ise) istekohta või (loosida)? "))
if istekoha_valik == "ise":
    istekoht_aken = str(input("Kas soovite (akna) all istuda või (muu) soovi? "))
if istekoha_valik == "ise"and istekoht_aken == "akna":
    print(str("Valisite istekoha akna all."))
elif istekoha_valik == "ise"and istekoht_aken == "muu":
    print(str("Valisite muu istekoha."))
if istekoha_valik == "loosida":
    from random import randint
    akna_all = randint(1, 3)
    if akna_all == 2:
        print(str("Loosisite istekoha akna all."))
    elif akna_all == 3:
        print(str("Loosisite istekoha vasakpoolses reas."))
    
    

        

    
    
    
    
    








                          
                    

    

    