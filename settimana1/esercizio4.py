#esercizio 4
def pullman_necessari(n):
    pullman = n // 53
    if n % 53 > 0:
        return pullman + 1
    return pullman

for n in [53, 54, 106]:
    print(f"Per {n} studenti servono {pullman_necessari(n)} pullman")

