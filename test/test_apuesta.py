from classApuesta import Apuesta
import pytest
def test_prueba():
    assert(True)


def test_constructor():
    a = Apuesta()
    assert(a.fichas==0)

def test_repr():
    a = Apuesta()
    msj = a.__repr__()
    assert("Apuesta" in msj)
    assert("Fichas" in msj)
    assert("0" in msj)

def test_ponerFicha():
   
    a = Apuesta()
    a.ponerficha(1)
    assert(a.fichas == 1)
    
    a = Apuesta()
    a.ponerficha(2)
    assert(a.fichas == 2) 


def test_ponerFichaVarias():
    a = Apuesta()
    a.ponerficha(2) 
    a.ponerficha(3)
    assert(a.fichas == 5)
    

def test_tomarFicha_valor_sin_argumentos():
    a = Apuesta()
    a.fichas = 5
    a.tomarficha()
    assert(a.fichas == 4)


def test_tomarFichaError():
    with pytest.raises(ValueError):
        a = Apuesta()
        a.fichas = 5
        a.tomarficha(6)
    
    a = Apuesta()
    a.fichas = 5
    a.tomarficha(5)
    assert(a.fichas==0)

def test_tomarTodas():
    a = Apuesta()
    a.ponerficha(0)
    a.ponerficha(1)

    assert(a.fichas==a.fichas)

def test_tieneFicha():
    a = Apuesta()

    a.ponerficha(1)
    assert(a.fichas > 0)

def test_estaVacio():
    a = Apuesta()
    a.ponerficha(1)
    a.tomarficha(1)

    assert(a.fichas==0) 