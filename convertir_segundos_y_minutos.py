""" Script en Python que implemente un programa para realizar
    las siguientes conversiones:
    - segundos a minutos: recibe segundos y devuelve minutos y segundos
    - segundos a horas: recibe segundos y regresa horas, minutos y segundos
    - minutos a segundos: recibe minutos y segundos y devuelve segundos
    - minutos a horas: recibe minutos y segundos, y devuelve horas, minutos y segundos

    ademas deberá implementarse un método para imprimir el menú de opciones y la ejecución
    del programa debe comenzar desde el procedimiento "main". El programa debe
    seguir en ejecución mientras el usuario no decida salir.
"""
import os

SEGUNDOS_POR_MINUTOS = 60
MINUTOS_POR_HORA = 60
SEGUNDOS_A_MINUTOS = 1
SEGUNDOS_A_HORAS = 2
MINUTOS_A_SEGUNDOS = 3
MINUTOS_A_HORAS = 4
SALIR = 0

def segundos_a_minutos(segundos):
    mins = segundos // SEGUNDOS_POR_MINUTOS
    segs = segundos % SEGUNDOS_POR_MINUTOS

    return mins, segs

def minutos_a_segundos(minutos, segundos):
    segs = minutos * SEGUNDOS_POR_MINUTOS + segundos

    return segs

def minutos_a_horas(minutos, segundos):
    hrs = minutos // MINUTOS_POR_HORA
    mins = minutos % MINUTOS_POR_HORA
    segs = segundos

    return hrs, mins, segs

def segundos_a_horas(segundos):
    mins, segs = segundos_a_minutos(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)

    return hrs, mins, segs

def menu():
    print(f""" Conversiones
    {SEGUNDOS_A_MINUTOS}) segundos a minutos
    {SEGUNDOS_A_HORAS}) segundos a horas, minutos y segundos
    {MINUTOS_A_SEGUNDOS}) Minutos y segundos a segundos
    {MINUTOS_A_HORAS}) Minutos y segundos a horas, minutos y segundos
    {SALIR}) salir""")


def main():
    continuar = True
    while continuar:
        os.system('cls')
        menu()
        opc = int(input('Selecciona una opción: '))
        os.system('cls')
        if opc == SEGUNDOS_A_MINUTOS:
            s = -1
            while 0 > s:
                s = int(input('Cantidad de segundos a convertir: '))
            mins, segs = segundos_a_minutos(s)
            print(f'El equivalente es: {mins}:{segs}')
        elif opc == SEGUNDOS_A_HORAS:
            s = -1
            while 0 > s:
                s = int(input('Cantidad de segundos a convertir: '))
            hrs, mins, segs = segundos_a_horas(s)
            print(f'El equivalente es: {hrs}:{mins}:{segs}')
        elif opc == MINUTOS_A_SEGUNDOS:
            m = -1
            while 0 > m:
                m = int(input('Cantidad de minutos a convertir: '))

            s = -1
            while 0 > s or s > SEGUNDOS_POR_MINUTOS:
                s = int(input('Cantidad de segundos a convertir: '))

            segs = minutos_a_segundos(m, s)
            print(f'El equivalente es: {segs}')
        elif opc == MINUTOS_A_HORAS:
            m = -1
            while 0 > m:
                m = int(input('Cantidad de minutos a convertir: '))

            s = -1
            while 0 > s or s > SEGUNDOS_POR_MINUTOS:
                s = int(input('Cantidad de segundos a convertir: '))

            hrs, mins, segs = minutos_a_horas(m, s)
            print(f'El equivalente es: {hrs}:{mins}:{segs}')
        elif opc == SALIR:
            print('Nos vemos...')
            continuar = False
        else:
            print('Opción no válida.')

        input('Presiona enter para continuar...')



if __name__ == '__main__':
    main()




