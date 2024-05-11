import numpy as np
import random as rd

#Funcion donde se escoge al primero y segundo con mayor puntaje
def PartidoGrupos(equipos):
    resultados = np.array([])
    Primeros = np.array([])
    for equipo in equipos:
        resultado_parcial = np.random.choice(puntaje, 6)
        suma = resultado_parcial.sum()
        resultados=np.append(resultados, suma)
    Primeros = np.append(Primeros, equipos[np.argmax(resultados)])
    Primeros = np.append(Primeros, equipos[np.argsort(resultados)[-2]])
    return Primeros

#Funcion que emula una cantidad de partidos seleccionando a los equipos que se enfrentan de
#manera aleatoria
def Partidos(lista_de_equipos, lista_de_clasificados, cantidad_de_partidos):
    np.random.shuffle(lista_de_equipos)
    numero_de_equipo = 0
    for partido in list(range(1,cantidad_de_partidos+1)):
        equipo1_goles = rd.randint(0,5)
        equipo2_goles = rd.randint(0,5)
        if equipo1_goles < equipo2_goles:
            lista_de_clasificados = np.append(lista_de_clasificados, lista_de_equipos[0+numero_de_equipo])
            numero_de_equipo += 2
        elif equipo1_goles > equipo2_goles:
            lista_de_clasificados = np.append(lista_de_clasificados, lista_de_equipos[1+numero_de_equipo])
            numero_de_equipo += 2
        else:
            lista_de_clasificados = np.append(lista_de_clasificados, lista_de_equipos[rd.randint(0,1)+numero_de_equipo])
    return lista_de_clasificados


#Copa Paceña
#Definimos los equipos, el puntaje que se puede obtener en la seleccion de grupos, las listas
#que despues llenaremos con los equipos que clasificaran, y una variable que nos ayudara al momento
#de añadir el equipo que gano en cuartos, semifinales y la final ya que se sumara al indice
grupo1_equipos = np.array(["The Strongest", "Millonarios", "Real Santa Cruz", "San Antonio"])
grupo2_equipos = np.array(["Aurora", "Nacional Potosí", "Blooming", "Royal Pari"])
grupo3_equipos = np.array(["Always Ready", "Guabira", "Independiente Petrolero", "FC Universitario"])
grupo4_equipos = np.array(["Bolívar", "San Jose", "Jorge Wilstermann", "Oriente Petrolero"])
puntaje = np.array([0, 1, 3])
cuartos_equipos = np.array([])
semifinal_equipos = np.array([])
final_equipos = np.array([])
ganador = np.array([])

#Ejecutamos las funciones y añadimos los resultados a la lista de los equipos que pasaron a cuartos
cuartos_equipos = np.append(cuartos_equipos, PartidoGrupos(grupo1_equipos))
cuartos_equipos = np.append(cuartos_equipos, PartidoGrupos(grupo2_equipos))
cuartos_equipos = np.append(cuartos_equipos, PartidoGrupos(grupo3_equipos))
cuartos_equipos = np.append(cuartos_equipos, PartidoGrupos(grupo4_equipos))
print(f"""Los equipos clasificados a cuartos son
{cuartos_equipos}
""")

#Ejecutamos la funcion para los 4 partidos de cuartos donde sacaremos la lista de clasificados
semifinal_equipos = Partidos(cuartos_equipos, semifinal_equipos, 4)
print(f"""Los equipos clasificados a las semifinales son
{semifinal_equipos}
""")

#Ejecutamos la funcion para los partidos de semifinales
final_equipos = Partidos(semifinal_equipos, final_equipos, 2)
print(f"""Los equipos clasificados a las finales son
{final_equipos}
""")

#Ejecutamos la funcion para el ganador de la copa
ganador = Partidos(final_equipos, ganador, 1)
print(f"El ganador de la copa es {ganador[0]}!!")

#El codigo no contempla solucion al caso de seleccion de primer y segundo lugar al mismo equipo
#en los equipos seleccionados de grupos
