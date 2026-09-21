#esercizio 5

def statistiche(voti):
    if len(voti) == 0:
        return None, None, None
    min = voti[0]
    max = voti[0]
    for n in voti:
        if(n < min):
            min = n
        if(n > max):
            max =  n
    media = sum(voti) / len(voti)
    return min, max, media

minimo, massimo, med = statistiche([6, 9, 7, 5])
print(f"min {minimo}, max {massimo}, media {med}")

print(statistiche([]))