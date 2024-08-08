a = "Ciao"

# IN QUESTO MODO NOI VERIFICHIAMO SE a HA CONTENUTO O MENO!
# Quindi se ad a metto "ciao" dara' VERO! se invece ad a metto ""
# quindi lascio la stringa vuota dara' Falso!
if a: 
    print("Vero!")
else:
    print("Falso!")
    
maghi = ["Harry", "Ron", "Hermione"]
for mago in maghi :
    # continue and break
    # print(mago)
    if mago == "Ron":
        #SALTA TUTTO QUELLO CHE VIENE DOPO
        # continue
        #SI BLOCCA TUTTO ALL'ARRIVO DELLA STRINGA "RON"
        break
    print(mago)

#STAMPA LA PAROLA INSERITA TRA LE "" UNO AD UNO!
for lettera in "Silente":
    print(lettera)
    
#STAMPA TUTTI I NUMERI DA 0 A 4!
for i in range(5):
    print(i)
    
import random

print(random.random())
print(random.randint(1,3))
print(random.choice(maghi))

import os

print(os.listdir())
