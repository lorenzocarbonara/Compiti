stipendi_totali=0
numero_stipendi=0
while true:
    stipendio=input("Salve, inserisci il valore dello stipendio")
    if stipendio=="-1":
        break
    else:
        stipendio=int(stipendio)
        stipendi_totali+=stipendio
        numero_stipendi+=1
media_stipendi=int(stipendi_totali/numero_stipendi)
print("la media in euro degli stipendi è di:", media, "€")
