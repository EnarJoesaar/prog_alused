inimeste_arv = int(input("Sisestage inimeste arv:"))
kohtade_arv = int(input("Sisestage kohtade arv ühes bussis:"))
bussid = inimeste_arv // kohtade_arv
mahajäänud = inimeste_arv % kohtade_arv
if mahajäänud > 0:
    bussid = bussid + 1
print("Tuleb tellida " +  str(bussid) + " bussi.")
