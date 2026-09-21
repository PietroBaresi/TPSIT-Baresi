voti = [4, 7, 5, 8, 6, 3]
voti_inizio = []

def sufficienze(voti):
    return [voto for voto in voti if voto >= 6]

print(sufficienze(voti))
print(sufficienze(voti_inizio))