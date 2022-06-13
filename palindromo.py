
def palindromo():
    print("ingresa una palabra para saber si es palíndromo.")
    palabra = input("Ingresa la palabra: ")

    invertida = "".join(reversed(palabra))
    if palabra == invertida:
        print("Es palíndromo")
        print(f"{palabra} = {invertida}")
    else:
        print("No es palíndromo")
        print(f"{palabra} != {invertida}")


palindromo()