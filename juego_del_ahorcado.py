""" Crear el juego del ahorcado. para este programa el usuario
    deberá adivinar uno de los 35 paises de américa.

    el juego debe comenzar seleccionando de forma aleatoria el
    nombre del país. los nombres deberan estar almacenados en una lista.
    Una vez seleccioando el país, se le mostrará al usuario una cadena
    compuesta de tantos guiones bajos como letrar tenga el nombre del país.

    A partir de ahí el usuario debe intentar adivinar las letras que conforman
    el nombre teniendo hasta 5 fallos máximo. si el usuario propone una letra
    y se encuentra en el nombre, entonces se remplaza todas las ocurrencias
    de esa letra en la palabra secreta.

    El juego termina cuando se ha descubierto la palabra o el usuario falló
    más de 5 veces.
"""

import random
import os

MAX_FALLOS = 5

paises = ['Estados Unidos', 'Brasil', 'México', 'Canadá', 'Argentina', 'Colombia', 'Chile', 'Perú', 'República Dominicana', 'Ecuador', 'Guatemala', 'Venezuela', 'Panamá', 'Cuba', 'Costa Rica', 'Bolivia', 'Paraguay', 'Uruguay', 'El Salvador','Honduras', 'Nicaragua','Trinidad y Tobago','Haití', 'Jamaica', 'Guyana', 'Bahamas', 'Surinam', 'Barbados', 'Belice', 'Santa Lucía', 'Antigua y Barbuda', 'Granada', 'San Vicente y las Granadinas', 'San Cristóbal y Nieves', 'Dominica']

def crearCadena():
    pais = random.choice(paises)
    secreto = '_'*len(pais)

    return pais, secreto


def reemplazarSimbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos+1:]
        inicio = pos + 1
    return secreto


def ahorcado():
    print('                             Juego del ahorcado')
    print(f'Debes adivinar cuál país de America es, \
dentro de los {len(paises)} que hay. \
Tienes {MAX_FALLOS} fallos. Suerte!')
    input('Presiona enter para comenzar...')
    original, secreto = crearCadena()
    fallos = 0
    while secreto != original and fallos <= MAX_FALLOS:
        os.system('cls')
        print(f'Palabra: {secreto}')
        usuario = input('Escribe una letra que creas que esté en la palabra: ')
        if usuario in original:
            secreto = reemplazarSimbolo(original, secreto, usuario)
            print(f'\nBien hecho! la letra {usuario} es parte de la palabra.')
            # print(f'Palabra: secreto')
        else:
            print(f'\nLa letra {usuario} no se encuentra en el país secreto.')
            fallos += 1
            print(f'Llevas un total de {fallos} fallos.')
        input('\nPresiona enter para continuar...')
    os.system('cls')
    if secreto == original:
        print(f'\nFelicidades, descubriste el pais secreto!! {original}')
    else:
        print(f'\nlo siento, has perdido. el país era {original}.')

    print('\nFin del programa.')


def main():
    ahorcado()


if __name__ == '__main__':
    main()


