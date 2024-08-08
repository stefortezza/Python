# LE CONSTANTI SI SCRIVONO IN MAIUSCOLO
ANNO_AVVIO_NEGOZIO = 2024
veicolo_offerta = "Bici elettrica"
prezzo_offerta = 190.90
veicolo_disponibile = True

print("Benvenuti al negozio Epic Bikes!")
# MODIFICA DI UNA CONSTANTE
# ANNO_AVVIO_NEGOZIO +=2 

# IN QUESTO MODO CI STAMPA IL TIPO 
print( type(ANNO_AVVIO_NEGOZIO))

# IN QUESTO MODO CAMBIAMO IL TIPO IN FLOAT
print( type(float(ANNO_AVVIO_NEGOZIO)))

# IN QUESTO MODO NON ABBIAMO ERRORI PERCHE' STIAMO CONCATENANDO DUE STRINGHE
print("Non perderti l'offerta sulla nostra: " + veicolo_offerta)

# IN QUESTO MODO DOBBIAMO INSERIRE PRIMA str PER NON AVERE ERRORI 
# POICHE' STIAMO CONCATENANDO UNA STRINGA AD UN INT.
# QUINDI DOBBBIAMO CASTARLA IN str PER CONCATENARLA CORRETTAMENTE.
print("Provala subito al prezzo di € " + str(prezzo_offerta))

# SECONDO METODO PER CONCATENARE UNA STRINGA AD UN INT
print(f"Provala subito al prezzo di € {prezzo_offerta}")

biciclette = ["Mountain bike", "Graziella", "BMX", "Triciclo"]
motociclette = ["Vespa", "Harley", "Ciao", "Apixedda"]

# STAMPA TUTTO L'ARRAY 
print("STAMPIAMO TUTTE LE BICICLETTE: " + str(biciclette))

# CICLIAMO GLI ELEMENTI DELL'ARRAY AD UNO AD UNO!
for bicicletta in biciclette:
    print("STAMPIAMO OGNI SINGOLO ELEMENTO DELL'ARRAY: " + "-" + bicicletta)

print()

for bicicletta in enumerate(biciclette): 
    print("STAMPIAMO OGNI SINGOLO ELEMENTO DELL'ARRAY MA ADESSO NUMERATO: " + str(bicicletta))

print("Inserisci il tuo anno di nascita")   
anno_nascita = int(input())
anni_cliente = 2024 - anno_nascita
print("Annni del cliente: " + str(anni_cliente))

# CONTROLLIAMO SE GLI ANNI SONO MAGGIORI O UGUALI A 18, IN TAL CASO
# STAMPA SE SEI MAGGIORENNE O MINORENNE.
if anni_cliente < 18 : 
    print("Sei minorenne")
    veicoli = biciclette
else:
    print("Sei maggiorenne")
    veicoli = biciclette + motociclette
    
print(veicoli)

# AGGIUNTIAMO UN ELEMENTO AD UN ARRAY CON IL METODO .APPEND
veicoli.append("Tandem")
print(veicoli)