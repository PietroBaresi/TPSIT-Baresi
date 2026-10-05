f = open("appunti.txt", "w", encoding="utf-8")
f.write("prima riga\n")

# il file non è ancora chiuso: proviamo a rileggerlo
print("prima di close:", repr(open("appunti.txt", encoding="utf-8").read()))

f.close()
print("dopo close:  ", repr(open("appunti.txt", encoding="utf-8").read()))


try:
    with open("appunti.txt", "w", encoding="utf-8") as f:
        f.write("prima riga\n")
        print("dentro il with, chiuso?", f.closed)
        1 / 0
except ZeroDivisionError:
    print("il programma è andato in errore")

print("fuori dal with, chiuso?", f.closed)
