def senza_duplicati(elementi):
    presenti = set()
    non_doppi = []
    for e in elementi:
        if e not in presenti:
            presenti.add(e)
            non_doppi.append(e)
    return non_doppi

nomi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
print(senza_duplicati(nomi))