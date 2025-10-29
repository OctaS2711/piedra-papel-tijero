
## Array principal que sostiene las manos, ArrayManoEnEspecifico=[ 0=> NombreMano, 1=>ArrayGana, 2=>ArrayPierde]
import random
manos = [
    [
        "PAPEL", # Nombre Mano
        ["PIEDRA","SPOCK"], # Array Contra que gana Papel
        ["TIJERA", "LAGARTO"] # Array Contra que pierde Papel
    ],
    [
        "TIJERA",
        ["PAPEL", "LAGARTO"],
        ["PIEDRA","SPOCK"]
    ],
    [
        "PIEDRA",
        ["TIJERA", "LAGARTO"],
        ["PAPEL","SPOCK"]
    ],
    [
        "SPOCK",
        ["TIJERA","PIEDRA"],
        ["PAPEL", "LAGARTO"]
    ],
    [
        "LAGARTO",
        ["PAPEL","SPOCK"],
        ["PIEDRA", "TIJERA"]
    ]
]




def elegirMano():
    contador = 0
    for x in range(len(manos)):
        print(str(contador) + ": " + str(manos[x][0]))
        contador += 1

    manoElegida = int(input("¿Que mano quiere jugar?\n"))

    return manos[manoElegida]

def elegirManoMaquina():
    manoElegida = random.randint(0, len(manos) - 1)
    return manos[manoElegida]


def jugar(puntos, puntosMaquina):
    
    manoMaquina = elegirManoMaquina()
    print(manoMaquina) ## TODO: Eliminar este print
    manoHumana = elegirMano()
    
    if manoMaquina == manoHumana:
        return puntos, puntosMaquina

    nombreManoHumano = manoHumana[0]
    arrayGanadorMaquina = manoMaquina[1]
    
    for i in range(len(arrayGanadorMaquina)):
        if nombreManoHumano == arrayGanadorMaquina[i]:
            puntosMaquina = puntosMaquina + 1
            return puntos, puntosMaquina
        i = i + 1

    puntos = puntos + 1
    return puntos, puntosMaquina


#codigo base
ganaCon = int(input("INGRESE A CUANTOS PUNTOS VA A JUGAR \n"))
if ganaCon == 0:
    print("No se juega, fin del programa")
else:
    puntos = 0
    puntosMaquina = 0
    while puntos != ganaCon and puntosMaquina != ganaCon:
        puntos, puntosMaquina = jugar(puntos, puntosMaquina)
        print(puntos, puntosMaquina)
    
print("FIN DE JUEGO")