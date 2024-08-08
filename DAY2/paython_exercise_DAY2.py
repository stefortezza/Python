import random

print("Benvenuto al gioco!")
nome_giocatore = input("Per favore, inserisci il tuo nome: ")
modalita_invincibile = input("Vuoi la modalita' INVINCIBILE? ").lower() == "si"
if modalita_invincibile:
    print("Modalita' INVINCIBILE attiva")
else:
    print("Modalita' INVINCIBILE inattiva")
    
print(f"Benvenuto {nome_giocatore} in questa nuova sfida di CARTA FORBICI SASSO, quante partite vuoi giocare?")
numero_partite = int(input("Per favore, inserisci il numero di partite: "))
possibile_scelta = ["carta", "forbici", "sasso"]

vittorie_giocatore = 0
vittorie_computer = 0

for numero_partita in range(numero_partite):
    print(f"\nPartita {numero_partita + 1} di {numero_partite}")
    print("Scegli tra: " + str(possibile_scelta).lower())
    scelta_giocatore = input().lower()

    if scelta_giocatore not in possibile_scelta:
        print("Scelta non valida! Il gioco verra' terminato.")
        break  # Esce dal ciclo se la scelta non è valida
    
    if modalita_invincibile:
        if scelta_giocatore == "carta":
            scelta_random = "sasso"
        elif scelta_giocatore == "forbici":
            scelta_random = "carta"
        elif scelta_giocatore == "sasso":
            scelta_random = "forbici"
    else:
        scelta_random = random.choice(possibile_scelta)

    print(f"Il computer ha scelto: {scelta_random}")

    if scelta_giocatore == scelta_random:
        risultato = "Pareggio!"
    elif (scelta_giocatore == "carta" and scelta_random == "sasso") or \
         (scelta_giocatore == "forbici" and scelta_random == "carta") or \
         (scelta_giocatore == "sasso" and scelta_random == "forbici"):
        risultato = f"{nome_giocatore} VINCE!"
        vittorie_giocatore += 1
    else:
        risultato = "Computer VINCE!"
        vittorie_computer += 1

    print(f"Risultato: {risultato}")
    print(f"Punteggio attuale: {nome_giocatore} - {vittorie_giocatore}, Computer - {vittorie_computer}")

if vittorie_giocatore > vittorie_computer:
    print(f"{nome_giocatore} e' il vincitore finale!")
elif vittorie_giocatore < vittorie_computer:
    print("Il computer e' il vincitore finale!")
else:
    print("Il gioco e' finito in pareggio!")

print(f"Alla prossima, {nome_giocatore}!")
