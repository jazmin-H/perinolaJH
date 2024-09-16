from classPerinola import Perinola 

def test_prueba():
    assert(True)

def test_constructor():
    p = Perinola()
    assert(p.cara_visible == p.cara_visible)

def test_repr():
    p = Perinola()
    msj = p.__repr__()
    assert("Salio:" in msj)
    assert(p.cara_visible in msj)

def test_tirar():
    p = Perinola()
    tirar = p.tirar()
    assert(p.cara_visible == tirar)