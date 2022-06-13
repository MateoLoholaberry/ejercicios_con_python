import random

def piedra_papel_tijera():
    print("\n                 Bienvenido al juego de piedra, papel o tijeras")

    opciones = ["pi", "pa", "ti"]

    usuario = input("Selecciona piedra (PI), papel (PA) o tijeras (TI) (Escibre tu opción): ").lower()

    compu = random.choice(opciones)

    print(f"Tu selección es: '{usuario}' y la de la compu es: '{compu}'\n")

    if usuario == compu:
        return "Empate!!"

    if gano_el_jugador(usuario, compu):
        return "Ganaste!!"
    else:
        return "Perdiste!! :("


def gano_el_jugador(jugador, oponente):
    #Retorna True si el jugador ganó

    if ((jugador == "pi" and oponente == "ti")
        or (jugador == "pa" and oponente == "pi")
        or (jugador == "ti" and oponente == "pa")):
        return True
    else:
        return False


print(piedra_papel_tijera())