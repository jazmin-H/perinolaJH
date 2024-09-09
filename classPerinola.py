from random import choice
class Perinola:
    caras = ('Pon 1','Pon 2','Toma 1','Toma 2',
            'Todos Toman','Ponen Todos')
    def __init__(self):
     self.cara_visible = choice(self.caras) 
    def __repr__(self):
        return f"Salio: {self.cara_visible}"
    def tirar(self):
        caras = [1, 2, 3, 4, 5, 6]
        self.cara_visible = choice(caras)
        return self.cara_visible