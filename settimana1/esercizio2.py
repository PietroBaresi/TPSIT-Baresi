#esercizio 2
def e_pari(n):
    return n % 2 == 0
    
for i in range(20):
    if(e_pari(i)):
        print(f"{i}")

