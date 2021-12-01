def kuu(jarjekord):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[int(jarjekord) - 1]
def kuupäev_sõnena(kuupäev):
    kuupäevad = kuupäev.split(".")
    kuupaev = kuupäevad[0] + ". " + kuu(int(kuupäevad[1])) + " " + kuupäevad[2] + ". a"
    return kuupaev

kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(kuupäev_sõnena(kuupäev))