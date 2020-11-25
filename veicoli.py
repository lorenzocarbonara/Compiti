numero_veicoli=0
print("Per fermare le domande digitare 0")
while True:
    flusso_veicoli=int(input("In questa giornata quanti sono i veicoli che hanno attraversato il casello?"))
    if flusso_veicoli==0:
        break
print("Hanno attraversato il casello", flusso_veicoli, "veicoli")