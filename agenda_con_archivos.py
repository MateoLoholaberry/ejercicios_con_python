""" Script en Python que implemente una agenda de contactos haciendo uso
    de un diccionario. Para el diccionario las llaves serán los nombres
    de los contactos, y como valor estará una tupla que contenga el número
    telefónico y el correo electrónico. La agenda se guardará en archivo
    de texto del cuál se podrán recuperar contactos y en el cual se podrán
    agregar los nuevos contactos registrados. Se tendrá un menú con las
    siguientes opciones:

    1) Agregar contacto
    2) Mostrar contactos
    3) Buscar contacto
    0) Salir
"""

import os
import pathlib

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3


def mostrar_menu():
    os.system('cls')

    print(f"""                  Mi Agenda
    {AGREGAR}) Agregar contacto
    {MOSTRAR}) Mostrar contacto
    {BUSCAR}) Buscar contacto
    {SALIR}) Salir""")

def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefault(contacto, (telefono, email))
    else:
        with open(nombre_archivo, 'w') as archivo:
            pass

def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('                 Agregar contacto')
    nombre = input('Nombre del contacto: ')

    if agenda.get(nombre):
        print('El contacto ya existe.')
    else:
        telefono = input('Teléfono: ')
        email = input('Email: ')
        agenda.setdefault(nombre, (telefono, email))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f'{nombre}, {telefono}, {email}\n')
        print('Contacto agregado con éxito.')

def mostrar_contactos(agenda):
    os.system('cls')
    print('                     Mis contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Teléfono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('*'*30)
    else:
        print('No hay contactos registrados.')

def buscar_contacto(agenda):
    os.system('cls')
    print('                     Buscar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre a buscar: ')
        cont = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Teléfono: {datos[0]}')
                print(f'Email: {datos[1]}')
                cont += 1
                print('*'*30)
        if cont == 0:
            print('No se encontraron contactos.')
        else:
            print(f'Se encontraron {cont} contactos.')
    else:
        print('No hay contactos registrados.')

def main():
    mi_agenda = {}
    continuar = True
    nombre_archivo = 'agenda.txt'
    cargar_agenda(mi_agenda, nombre_archivo)

    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opción: '))
        if opc == AGREGAR:
            agregar_contacto(mi_agenda, nombre_archivo)
        elif opc == MOSTRAR:
            mostrar_contactos(mi_agenda)
        elif opc == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida.')

        input('Presiona enter para continuar...')
    print('\nFin del programa.')


if __name__ == '__main__':
    main()
