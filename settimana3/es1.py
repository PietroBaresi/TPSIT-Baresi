def salva_appunto(testo):
    with open("appunti.txt", "w", encoding="utf-8") as f:
        f.write(testo + "\n")

salva_appunto("Ciao a tutti")
salva_appunto("Come state")
salva_appunto("Ricordatevi i commit")

with open("appunti.txt", "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start = 1):
        print(numero, riga.split())