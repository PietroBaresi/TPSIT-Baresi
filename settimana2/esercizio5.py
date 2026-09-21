def conta_parole(frase):
    conteggio = {}
    for parola in frase.lower().split():
        conteggio[parola] = conteggio.get(parola, 0) + 1
    return conteggio

frase = "il gatto dorme il cane dorme il topo corre"
risultato = conta_parole(frase)
print(risultato)

piu_frequente = max(risultato, key=risultato.get)
print(piu_frequente, risultato[piu_frequente])
