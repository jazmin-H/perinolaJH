class Jugador:
 def __init__(self, nombre = "x", fichas = 5):
     self.nombre = nombre
     self.fichas = fichas
 def __repr__(self):
    return f"{self.nombre} tiene {self.fichas} fichas"
 def darFicha (self, cuantas = 1):
    self.fichas = self.fichas + cuantas
 def sacarFicha (self, cuantas = 1):
    if self.fichas < cuantas :
     raise ValueError("mal, la cantidad de fichas es menor a lo q se quiere sacar")
    self.fichas = self.fichas - cuantas
 def tieneFicha(self, cuantas = 1):
    return self.fichas >= cuantas
 def sinFichas(self): 
    return self.fichas == 0

