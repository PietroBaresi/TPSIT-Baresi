#import json


# ''' dici a python che è un formato json
testo = '''{                                       
  "titolo": "Il deserto dei Tartari",
  "prezzo": 9.90,
  "anno": 1940,
  "disponibile": true,
  "ristampa": null,
  "generi": ["romanzo", "classico"],
  "editore": {"nome": "Mondadori", "citta": "Milano"}
}'''

#carica il testo in una variabile (che sarà un dizionario)
dati = json.loads(testo)

#14, 40 è per la tabulazione, cioè occupa 14 caratteri la chiave e se è più corta aggiunge spazi, stessa cosa per valore
for chiave, valore in dati.items():
    print(f"{chiave:14} {str(valore):40} {type(valore).__name__}")

