primo_candidato=input("Salve, inserisci il nome del primo candidato").upper()
secondo_candidato=input("Ora procedi inserendo il nome del secondo candidato").upper()
punteggio_primo_candidato=int(input("Ineserire il punteggio del primo candidato"))
punteggio_secondo_candidato=int(input("Ora inserisci il punteggio del secondo candidato"))
if primo_candidato>secondo_candidato:
    print("Ecco l'ordine alfabetico dei candidati:", primo_candidato, secondo_candidato)
elif primo_candidato<secondo_candidato:
    print("ecco l'ordine alfabetico dei candidati:", secondo_candidato, primo_candidato)
if punteggio_primo_candidato>punteggio_secondo_candidato:
    print("In base al punteggio, l'ordine è:", primo_candidato, secondo_candidato, "ha vinto il primo candidato")
elif punteggio_primo_candidato<punteggio_secondo_candidato:
    print("In base al punteggio, l'ordine è:", secondo_candidato, primo_candidato, "ha vinto il secondo candidato")
elif punteggio_primo_candidato==punteggio_secondo_candidato:
    print("Si ha un pareggio")
