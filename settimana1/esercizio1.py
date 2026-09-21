#esercizio 1
def celsius_a_fahrenheit(gradi):
    return gradi * (9/5) + 32

for celsius in [0, 25, 100]:
    print(f"{celsius}°C corrispondono a  {celsius_a_fahrenheit(celsius)}°F")
