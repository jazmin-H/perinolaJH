from classJugador import Jugador

j = Jugador()

print(j)

j.darFicha(2)
print(j)

j.sacarFicha(3)
print(j)

tieneficha = j.tieneFicha()
print(tieneficha)

j.sacarFicha(4)
print(j)

sinficha =j.sinFichas()
print(sinficha)
