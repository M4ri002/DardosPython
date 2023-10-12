
# IMPORT BIBLIOTECA
import random
import time

#OBJETO JUGADOR Y FUNCIONES
class Jugadores():
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def Mostar(self):   # FUNCION QUE MUESTRA EL NOMBRE Y LA PUNTACION DEL JUGADOR
        printar = ("\n \nJugador: {} \nPuntuacion Actual: {}")
        print (printar.format(self.nombre, self.puntuacion))

    def TiroDardos(self):   # FUNCION QUE GUARDA LOS TIROS RANDOM DEL JUGADOR Y LO RESTA A LA PUNTUACION INICIAL
        tiro1 = random.randrange(50)
        tiro2 = random.randrange(50)
        tiro3 = random.randrange(50)
        print("Tiro 1: ",tiro1,"\nTiro 2: ",tiro2,"\nTiro 3: ",tiro3,"\n")
        self.puntuacion = self.puntuacion - tiro1 - tiro2 - tiro3
        print("[ Puntuacion restante: ",self.puntuacion," ]")
        return self.puntuacion

    def ControlPuntos(self,Puntos,Ronda):   # ESTA FUNCION CONTROLA SI LA PUNTUACION DE UN JUGADOR ES 0 O INFERIOR
        if Puntos <= 0:
            print("\n******************************************************")
            print(self.nombre,"GANA LA PARTIDA CON ",Puntos, " PUNTOS EN LA RONDA ",Ronda,"\n")
            print("******************************************************")


# VARIABLES
PuntuacionInicial = 121

# INPUTS
NombreJugador1 = input("Escriba el nombre del jugador 1: ")
NombreJugador2 = input("Escriba el nombre del jugador 2: ")
NombreJugador3 = input("Escriba el nombre del jugador 3: ")

# GUARDAR OBJETO
Jugador1 = Jugadores(NombreJugador1,PuntuacionInicial)
Jugador2 = Jugadores(NombreJugador2,PuntuacionInicial)
Jugador3 = Jugadores(NombreJugador3,PuntuacionInicial)


# CUERPO DEL CODIGO
cont = 1
Bool = True
while cont <= 3 and Bool == True:
    print("_______________________________________")
    print("_______________________________________")
    print("**** RONDA ",cont,"****")
    Jugador1.Mostar()
    temp1 = Jugador1.TiroDardos()
    time.sleep(1)
    Jugador2.Mostar()
    temp2 = Jugador2.TiroDardos()
    time.sleep(1)
    Jugador3.Mostar()
    temp3 = Jugador3.TiroDardos()
    if temp1 <= 0 or temp2 <= 0 or temp3 <= 0:
        if temp1 <= 0:
            Jugador1.ControlPuntos(temp1,cont)
        if temp2 <= 0:
            Jugador2.ControlPuntos(temp2,cont)
        if temp3 <= 0:
            Jugador3.ControlPuntos(temp3,cont)
        Bool = False
    elif cont == 3 and (temp1 > 0 or temp2 > 0 or temp3 > 0):
        print("\nNADIE HA LLEGADO A 0 PUNTOS O MENOS, TERMINA LA PARTIDA")
    cont += 1
