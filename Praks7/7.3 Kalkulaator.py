from easygui import *
arvud = 0
arv1 = 0
arv2 = 0
nupud = ["+" , "-" , "*"]
arv1 = integerbox("Sisestage esimene täisarv 1-10: ")
arv2 = integerbox("Sisestage teine täisarv 1-10: ")
arvutamine = buttonbox("Programmeerimine on ", choices = nupud)
if arvutamine == "+":
    arvud = int(arv1 + arv2)  
    msgbox("Teie tulemus on: " +  str(arvud))
elif arvutamine == "-":
    arvud = int(arv1 - arv2)
    msgbox("Teie tulemus on: " +  str(arvud))
elif arvutamine == "*":
    arvud = int(arv1 * arv2)
    msgbox("Teie tulemus on: " +  str(arvud))
                       
                       
                       
                       

