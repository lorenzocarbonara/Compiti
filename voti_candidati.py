voti1=int(input("salve, inserisca i voti del primo candidato"))
voti2=int(input("ora inserisca i voti del secondo candidato"))
voti_tot=voti1+voti2
percentuale_primo_candidato=int(voti1/voti_tot*100)
percentuale_secondo_candidato=int(voti2/voti_tot*100)
print("il primo candidato ha ricevuto", voti1,"voti su", voti_totali,". La percentuale è del", percentuale_primo_candidato,"%" )
print("il secondo candidato, invece, ha ricevuto", voti1,"voti su", voti_totali,". La percentuale è del", percentuale_secondo_candidato,"%" )
if voti1>voti2:
    print("il primo candidato ha ottenuto un numero maggiore di voti; in conclusione, è il vincitore")
elif voti1<voti2:ù
    print("il secondo candidato ha ottenuto un numero maggiore di voti; in conclusione, è il vincitore")
elif voti1==voti2
    print("il numero di voti è lo stesso, quindi si ha un pareggio")
print("grazie e arrivederci")
