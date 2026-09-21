#esercizio 3
def media(voti):
    if len(voti) == 0:
        return 0
    
    return sum(voti) / len(voti)
    
print(media([7, 8, 2, 10, 5]))
print(media([]))

