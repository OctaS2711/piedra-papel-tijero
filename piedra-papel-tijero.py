
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
    
    manoElegida = int(input("¿Que mano quiere jugar?\n \n" "JUGADOR: "))
    while manoElegida <0 or manoElegida > 4:  #controlo que el usuario no coloque seleccione un numero fuera del array (el array es de longitud 5, es decir que puede seleccionar del 0 al 4)
        print('por favor elegir una mano de las que figuran en pantalla \n Las opciones son del 0 al 4')
        manoElegida = int(input("¿Que mano quiere jugar?\n \n" "JUGADOR: "))
    return manos[manoElegida] 

def elegirManoMaquina():
    aux = 0
    manoElegida = random.randint(0, len(manos) - 1) 
    aux = manos[manoElegida][0]  #el primer corchete marca la fila y el segundo la columna de la matriz, esto me devuelve lo que esta en la columna, es decir la mano que juega el programa
    return manos[manoElegida], aux #me devuelve 2 valores, el auxiliar y el array
    

def jugar(puntos, puntosMaquina):
    
    
    manoMaquina, aux1 = elegirManoMaquina()
    manoHumana = elegirMano()
    print('MAQUINA: ',aux1)
    print()
    
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
ronda = 0 #variable contadora
print('BIENVENIDO A PIEDRA - PAPEL - TIJERA - LAGARTO - SPOCK')
print('REGLAS: ')
print()
print('* PIEDRA APLASTA AL LAGARTO / * PIEDRA ROMPE LA TIJERA')
print('* PAPEL TAPA LA PIEDRA / * PAPEL DESAUTORIZA A SPOCK')
print('* TIJERA CORTA AL PAPEL / * TIJERA DECAPITA AL LAGARTO')
print('* LAGARTO DEVORA AL PAPEL / * LAGARTO ENVENENA A SPOCK')
print('* SPOCK ROMPE LA TIJERA / * SPOCK VAPORIZA LA PIEDRA')
print()
ganaCon = int(input("INGRESE A CUANTOS PUNTOS VA A JUGAR \n"))
print()
while ganaCon < 0: #chequeo que no ingresen negativos
    print('POR FAVOR NO COLOCAR NUMEROS NEGATIVOS\n')
    ganaCon = int(input("INGRESE A CUANTOS PUNTOS VA A JUGAR \n"))
    print()

if ganaCon == 0: #si los puntos a jugar vale cero termina el programa
    print("No se juega, fin del programa")
else:
    puntos = 0
    puntosMaquina = 0
    while puntos != ganaCon and puntosMaquina != ganaCon: #ciclo hasta que o los puntos del usuario o de la maquina sean equivalentes a la cantidad de puntos a ganar
        ronda = ronda + 1
        print('RONDA N.° ', ronda)
        puntos, puntosMaquina = jugar(puntos, puntosMaquina)
        print('PUNTOS: ',puntos, ' - ', puntosMaquina)
        print()

    if puntos > puntosMaquina: #comparo los puntos para ver quien gano
        print('¡¡FELICIDADES, GANASTE!!')
        print()
        print('CANTIDAD DE RONDAS: ', ronda)
    else:
        print('GANO LA MAQUINA, SUERTE LA PROXIMA')
        print()
        print('CANTIDAD DE RONDAS: ', ronda)
        



print()
print("FIN DE JUEGO")
