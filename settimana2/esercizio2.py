capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

def capitale(paese):
    return capitali.get(paese, 'paese non in elenco')

print(capitale("Spagna"))
print(capitale("Germania"))