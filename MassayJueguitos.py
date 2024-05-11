import random

def JugarParOIpar():
    import random
    print("Seleccionaste jugar Par o Impar.")
    eleccion_jugador = input("Quieres par (P) o impar (I)? ").upper()
    if eleccion_jugador != 'P' and eleccion_jugador != 'I':
        print("No valido, seleccione de nuevo.")
        JugarParOIpar()
    resultado_dados = lanzarDados()
    suma = sum(resultado_dados)
    print("El resultado es:", resultado_dados)
    print("La suma es:", suma)
    if (suma % 2 == 0 and eleccion_jugador == 'P') or (suma % 2 != 0 and eleccion_jugador == 'I'):
        print("jugador 1 gano.")
        
def lanzarDados():
    import random
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return (dado1, dado2)

def JuegoMayorMenor():
    import random
    CartaJugador1=random.randint(1, 10)
    CartaJugador2=random.randint(1, 10)

    print("Jugador 1 tiene la carta: ",CartaJugador1)
    print("Jugador 2 tiene la carta: ",CartaJugador2)
    Eleccion1=MayoroMenor1()
    Eleccion2=MayoroMenor2()
    print("Jugador 1 dice: ", Eleccion1)
    print("Jugador 2 dice: ", Eleccion2)
    
    CartaMesa=random.randint(1, 10)
    
    if CartaMesa < CartaJugador1:
        if Eleccion1 == "Menor":
            print("Gana jugador 1")
        elif Eleccion1 == "Mayor":
            print("Pierde jugador 1")
    if CartaMesa < CartaJugador2:
        if Eleccion2 == "Menor":
            print("Gana jugador 2")
        elif Eleccion2 == "Mayor":
            print("Pierde jugador 2")
def MayoroMenor1():
    import random
    valor1=random.randint(1,2)
    if valor1== 1:
        return "Mayor"
    else:
        if valor1==2:
            return "Menor"
def MayoroMenor2():
    import random
    valor2=random.randint(1, 2)
    if valor2== 1:
        return "Mayor"
    else:
        if valor2==2:
            return "Menor"

def TurnoDeJugador(puntaje1, puntaje2):
    import random
    if puntaje1 > 21 and puntaje2 > 21:
        print("Ambos jugadores perdieron")
    elif puntaje1 > 21:
        print("El jugador 1 pierde")
    elif puntaje2 > 21:
        print("El jugador 2 pierde")
    elif puntaje1 > puntaje2:
        print("El jugador 1 gano el juego")
    elif puntaje1 < puntaje2:
        print("El jugador 2 gano el juego")
    else:
        print("Empate")
def TirarDados():
    import random
    puntaje1 = random.randint(1, 6)
    puntaje2 = random.randint(1, 6)
    print("Tu resultado es:", puntaje1)
    print("Tu resultado es:", puntaje2)
    return (puntaje1, puntaje2)
def JugarVeintiuno():
    print("Empieza el juego se jugaran 4 turnos")
    puntaje1 = 0
    puntaje2 = 0
    puntajes = TirarDados()
    puntaje1 += puntajes[0]
    puntaje2 += puntajes[1]
    print("Empieza el turno 2")
    puntajes = TirarDados()
    puntaje1 += puntajes[0]
    puntaje2 += puntajes[1]
    print("Empieza el turno 3")
    puntajes = TirarDados()
    puntaje1 += puntajes[0]
    puntaje2 += puntajes[1]
    print("Empieza el turno 4")
    puntajes = TirarDados()
    puntaje1 += puntajes[0]
    puntaje2 += puntajes[1]
    TurnoDeJugador(puntaje1, puntaje2) 


def turno(jugador1Carta, jugador2Carta):
    print(f"Jugador 1 tiro {jugador1Carta}, jugador 2 tiro {jugador2Carta}")
    if jugador1Carta < jugador2Carta:
        print("Jugador 2 gana esta ronda")
        puntajeJugador1 = 0
        puntajeJugador2 = 1
    elif jugador1Carta > jugador2Carta:
        print("Jugador 1 gana esta ronda")
        puntajeJugador1 = 1
        puntajeJugador2 = 0
    elif jugador1Carta == jugador2Carta:
        print("Es un empate, ningun jugador gana esta ronda")
        puntajeJugador1 = 0
        puntajeJugador2 = 0
    return (puntajeJugador1, puntajeJugador2)
    
    
    
def GuerraCartas():
    import random 
    print("""Bienvendio a Guerra de Cartas
Es simple, se juegan 5 turnos, cada jugador se le dan 5 cartas al inicio del juego, cada turno tiran una,
el jugador que tiro la carta con mas valor es el que gana""")
    puntajeJugador1 = 0
    puntajeJugador2 = 0
    posiblesCartas = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]
    random.shuffle(posiblesCartas)
    jugador1Cartas = [(posiblesCartas[0]), (posiblesCartas[1]), (posiblesCartas[2]), (posiblesCartas[3]), (posiblesCartas[4])]
    jugador2Cartas = [(posiblesCartas[4]), (posiblesCartas[5]), (posiblesCartas[6]), (posiblesCartas[7]), (posiblesCartas[8])]
    print("""----------------------
Se da el inicio del primer turno""")
    resultado = turno(jugador1Cartas[0], jugador2Cartas[0])
    puntajeJugador1 += resultado[0]
    puntajeJugador2 += resultado[1]
    print("""----------------------
Se da el inicio del segundo turno""")
    resultado = turno(jugador1Cartas[1], jugador2Cartas[1])
    puntajeJugador1 += resultado[0]
    puntajeJugador2 += resultado[1]
    print("""----------------------
Se da el inicio del tercer turno""")
    resultado = turno(jugador1Cartas[2], jugador2Cartas[2])
    puntajeJugador1 += resultado[0]
    puntajeJugador2 += resultado[1]
    print("""----------------------
Se da el inicio del cuarto turno""")
    resultado = turno(jugador1Cartas[3], jugador2Cartas[3])
    puntajeJugador1 += resultado[0]
    puntajeJugador2 += resultado[1]
    print("""----------------------
Se da el inicio del quinto turno""")
    resultado = turno(jugador1Cartas[4], jugador2Cartas[1])
    puntajeJugador1 += resultado[0]
    puntajeJugador2 += resultado[1]
    print("----------------------")
    ganador(puntajeJugador1, puntajeJugador2)
    
def ganador(puntaje1, puntaje2):
    if puntaje1 < puntaje2:
        print(f"Jugador 2 gana con {puntaje2} puntos")
    elif puntaje1 > puntaje2:
        print(f"Jugador 1 gana con {puntaje1} puntos")
    elif puntaje1 == puntaje2:
        print(f"Es un empate los dos cuentan con {puntaje1} puntos")


Juego = int(input("""Selecciona tu modo de juego
1. Guerra de Cartas
2. Mayor o menor (Cartas)
3. Par o impar (Dados)
4. Ventiuno (Dados)
"""))
if Juego == 1:
    GuerraCartas()
elif Juego == 2:
    JuegoMayorMenor()
elif Juego == 3:
    JugarParOIpar()
elif Juego == 4:
    JugarVeintiuno()