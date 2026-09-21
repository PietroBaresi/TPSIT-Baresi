#Lista
voti = [3, 5, 8, 9, 4, 7, 10, 7]
voti.append(8)                              #append inserisce in coda
voti.insert(2, 6)                           #insert inserisce il secondo elemento nella posizione del primo numero
print(voti)

print(voti[0], voti[-1])                    #[0] = primo elemento. "," fa stampare solo quelli che dici. [-1] è l'ultimo elemento
print(voti[0:4])                            #[0:4] da 0 a 4 escluso

voti.sort()                                 #riordina lista
print(voti)

print(len(voti), 8 in voti)


#Set
presenze = ["Luca", "Sara", "Marco", "Luca", "Sara"]
unici = set(presenze)                       #toglie i duplicati

print(len(presenze), "voci registrate")
print(len(unici), "persone diverse")
print(sorted(unici))                        #riordina i non duplicati

informatica = {"Luca", "Sara", "Marco"}
sistemi = {"Sara", "Giulia"}
print(sorted(informatica | sistemi))        # | significa unione dei non duplicati in ordine alfabetico
print(sorted(informatica & sistemi))        # & significa intersezione e stampa chi è presente in tutti e due
print(sorted(informatica - sistemi))        # - significa differenza e stampa chi c'è nel primo e non nel secondo
                                            # ^ significa differenza simmetrica	e stampa chi c'è in uno solo dei due

#Tuple -> è come una lista ma non si può modificare
week = ("lun", "mar", "mer", "gio", "ven")
print(week)
print(week[0], week[-1])
print(len(week))

try:
    week[0] = "dom"
except TypeError as errore:
    print("TypeError:", errore)

#Dizionario
capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

print(capitali["Italia"])
print(len(capitali))

capitali["Germania"] = "Berlino"            #aggiunge
del capitali["Spagna"]                      #elimina tutto spagna
print(capitali)

for paese, citta in capitali.items():
    print(paese, "->", citta)

print(list(capitali.keys()))                #keys stampa per esempio Italia che è la chiave di lettura
print(list(capitali.values()))              #values stampa per esempio Roma che è il valore


