print("Ciao a tutti")

nome = "Pietro"
eta = 17
altezza = 1.78
promosso = True
print(print(type(nome), type(eta), type(altezza), type(promosso)))
print(f"{nome} ha {eta} anni ed è alto {altezza} cm")
print(f"Fra due anni {nome} ne avrà {eta + 2}")

print(19 / 2)
print(19 // 2)
print(19 % 2)
print(5 ** 2)
print(int("42") + 3)
print("42" + "3")

voto = 6.5

if voto >= 6:
    esito = "sufficiente"
elif voto >= 5:
    esito = "insufficiente lieve"
else:
    esito = "insufficiente grave"

print(esito)

for i in range(3):
    print(f"giro {i}")

numeri = [4, 8, 15]
for n in numeri:
    print(n * 2)