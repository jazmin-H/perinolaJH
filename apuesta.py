class Apuesta:
 def __init__(self):
     self.ficha = 0
 def __repr__(self):
    return f"{self.ficha}"
 def ponerficha (self, cuantas = 1):
    self.ficha = self.ficha + cuantas
 def tomarficha (self, cuantas = 1):
    if self.ficha < cuantas :
        raise ValueError(f"mal, solo quedan {self.ficha}")
    self.ficha = self.ficha - cuantas  