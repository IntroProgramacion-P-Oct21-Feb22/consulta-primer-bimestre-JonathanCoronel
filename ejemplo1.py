"""
    Ejemplo 01
"""
nombre = input("¿Como te llamas? ")
genero = input("¿Cual es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)

