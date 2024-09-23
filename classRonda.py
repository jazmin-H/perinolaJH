from classJugador import Jugador
class Ronda:
 def __init__(self):
   self.jugadores = []
 def __repr__(self):
   return f"{self.jugadores}"
 def agregarJugador(self, jugador):
   if jugador.sinFichas <= 0:
     raise ValueError(f"jugador debe tener al menos 1 ficha para ser agregado")
   self.jugadores.append(jugador)
 