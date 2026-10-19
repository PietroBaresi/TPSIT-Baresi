import csv

def prezzo_medio(nome_file, alimentazione):
    somma = 0
    quantita = 0
    with open("dati/car_sales_data.csv", "r", encoding="utf-8", newline="") as f:
        for auto in csv.DictReader(f):
            if auto["Fuel type"] == alimentazione:
                somma += int(auto["Price"])
                quantita += 1
    if quantita == 0:
        return None
    return round(somma / quantita, 2)

for tipo in ["Petrol", "Diesel", "Hybrid", "Electrica"]:
    prezzo = prezzo_medio("dati/car_sales_data.csv", tipo)
    if prezzo is not None:
        print(f"Il prezzo medio delle auto {tipo} è: {prezzo} €")
    else:
        print(f"Nessuna auto {tipo} trovata.")