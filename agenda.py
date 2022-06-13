""" Script en python que implemente una agenda de contactos haciendo uso
    de un diccionario. Para el diccionario las llaves serán los nombres de
    los contactos y como valor estará una tupla que contenga un número
    telefónico y el correo electrónico. Se tendra un menú con las siguientes
    opciones:
    1) Agregar contactos
    2) Mostrar contactos
    3) Buscar contactos
    4) Modificar contacto
    5) Eliminar contacto
    0) Salir
"""

import os

AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5
SALIR = 0

def mostrar_menu():
    os.system('cls')
    print(f"""                        Agenda de contactos
{AGREGAR}) Agregar contacto
{MOSTRAR}) Mostrar contactos
{BUSCAR}) Buscar contacto
{MODIFICAR}) Modificar contacto
{ELIMINAR}) Eliminar contacto
{SALIR}) Salir
""")

def agregar_contacto(agenda):
    os.system('cls')
    print('                     Agregar contacto')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('Ya existe el contacto.')
    else:
        nro = int(input('Número: '))
        email = input('E-Mail: ')
        agenda.setdefault(nombre, (nro, email))
        print('El contacto se agregó con éxito.')

def mostrar_contactos(agenda):
    os.system('cls')
    print('                     Mostrar contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'telefono: {datos[0]}')
            print(f'E-Mail.: {datos[1]}')
            print('^'*20)
    else:
        print('No hay contactos registrados.')

def buscar_contacto(agenda):
    os.system('cls')
    print('                     Buscar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre del contacto: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Teléfono: {datos[0]}')
                print(f'E_Mail: {datos[1]}')
                print('^'*20)
                encontrados += 1
        if encontrados == 0:
            print('No se encontraron contactos.')
        else:
            if encontrados == 1:
                print(f'Se encontró {encontrados} contacto.')
            else:
                print(f'Se encontraron {encontrados} contactos.')
    else:
        print('No hay contactos registrados.')

def modificar_contacto(agenda):
    os.system('cls')
    print('                     Modificar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre del contacto a modificar: ')
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print('Información:')
            print(f'Nombre: {nombre}')
            print(f'Teléfono: {datos[0]}')
            print(f'E-Mail: {datos[1]}')
            print('^'*20)
            print('Ingresa los nuevos datos:')
            nro = int(input('Teléfono: '))
            email = input('E-Mail: ')
            agenda[nombre] = (nro, email)
            print('Datos actualizados con éxito.')
        else:
            print('No existe el contacto.')
    else:
        print('No hay contactos registrados.')

def eliminar_contacto(agenda):
    os.system('cls')
    print('                     Eliminar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            agenda.pop(nombre)
            print('Contacto eliminado con éxito.')
        else:
            print('No existe el contacto.')
    else:
        print('No hay contactos registrados.')


def main():
    continuar = True
    mi_agenda = {}
    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opción: '))
        if opc == AGREGAR:
            agregar_contacto(mi_agenda)
        elif opc == MOSTRAR:
            mostrar_contactos(mi_agenda)
        elif opc == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == MODIFICAR:
            modificar_contacto(mi_agenda)
        elif opc == ELIMINAR:
            eliminar_contacto(mi_agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida.')
        input('\nPresiona enter para continuar...')
    print('\nFin del programa.')


if __name__ == '__main__':
    main()