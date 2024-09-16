class Apuesta:
 def __init__(self):
     self.fichas = 0
 def __repr__(self):
    return f"Apuesta {self.fichas} Fichas"
 def ponerficha (self, cuantas = 1):
    self.fichas = self.fichas + cuantas
 def tomarficha (self, cuantas = 1):
    if self.fichas < cuantas :
        raise ValueError(f"mal, solo quedan {self.fichas}")
    self.fichas = self.fichas - cuantas 
 def tomarTodas(self): 
    tomar_todas = self.fichas
    return tomar_todas
 def tieneFicha(self, cuantas = 1):
    tiene_ficha = self.fichas >= cuantas
    return tiene_ficha
 def estaVacia(self):
    return self.fichas == 0 
   
       