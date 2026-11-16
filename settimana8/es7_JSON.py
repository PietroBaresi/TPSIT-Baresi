import json

def voto_medio(libro):
    recensioni = libro.get("recensioni", [])
    somma = 0
    if len(recensioni) == 0:
        return None
    for r in recensioni:
        somma += r["voto"]
    return round(somma / len(recensioni), 2)



with open("settimana8/programmi/libri.json", "r", encoding="utf-8") as f:
    libri = json.load(f)

classifica = []
for libro in libri:
    classifica.append({
        "titolo": libro["titolo"],
        "autore": libro["autore"],
        "voto_medio": voto_medio(libro),
        "quante_recensioni": len(libro.get("recensioni", [])),
    })

with open("settimana8/programmi/classifica.json", "w", encoding="utf-8") as f:
    json.dump(classifica, f, indent=2, ensure_ascii=False)

for riga in classifica:
    print(f"{riga['titolo']:26} {str(riga['voto_medio']):5} ({riga['quante_recensioni']} recensioni)")
