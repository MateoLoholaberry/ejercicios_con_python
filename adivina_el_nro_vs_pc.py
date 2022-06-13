import random
import os

def adivina_el_nro():
    print("\n                                               Bienvenido al juego de adivina el número.")
    print("\nSe generá un número aleatorio entre 1 y 100.")
    print("Tú y la máquina competirán por adivinarlo primero.")
    input("Presiona enter para continuar...")

    secreto = random.randint(1, 100)

    bandera = True
    menor = 1
    mayor = 100

    while bandera:
        os.system("cls")

        maquina = random.randint(menor, mayor)
        print(f"La maquina ha elegido el número {maquina}")

        if maquina > secreto:
            print("El número de la máquina es más grande que el secreto.")
            mayor = maquina - 1
        elif maquina < secreto:
            print("El número de la máquina es más chico que el número secreto.")
            menor = maquina + 1
        elif maquina == secreto:
            print("\nLa máquina ha acertado el número secreto!!!")
            print("¡La máquina ha ganado!")
            break

        try:
            usuario = int(input("\nAhora es tu turno, ingresa cual número crees que sea el secreto: "))
        except:
            print("\nSolo puedes ingresar números.")
            print("Has perdido tu turno.")
            input("Presiona enter para continuar.")
            continue

        if usuario > secreto:
            print("Tu numero es más grande que el número secreto.")
            if usuario < mayor:
                mayor = usuario - 1
        elif usuario < secreto:
            print("Tu numero es más chico que el número secreto.")
            if usuario > menor:
                menor = usuario + 1
        elif usuario == secreto:
            print("\nFelicidades has adivinado el número secreto!!!")
            print("¡Has ganado la partida!")
            input("Presiona enter para continuar...")
            break

        salir = input("\nSi deseas dejar de jugar presiona (s), sino presiona enter: ").lower()

        if salir == "s":
            print("\nHas abandonado la partida :(")
            print("Igualmente gracias por jugar.")
            print(f"El número secreto era: {secreto}")
            break
        else:
            pass

    print("\nFin del juego.")



adivina_el_nro()