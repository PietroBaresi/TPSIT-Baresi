import json

with open("settimana8/studenti.json", "r", encoding="utf-8") as f:
    print(f.read())

with open("settimana8/studenti.json", "r", encoding="utf-8") as f:
    riletta = json.load(f)
    print(type(riletta))