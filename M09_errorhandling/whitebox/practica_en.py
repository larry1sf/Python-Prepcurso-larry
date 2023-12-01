import unittest
import sys

sys.path.append(r"D:\vs\prepcuso\Python-Prepcurso-larry\M08_clasesyOOP")

import pr_depractica as pr

p1 = pr.suma(5, 2)


class Probando_excepciones(unittest.TestCase):
    # si no es falso cumple excepcion y muestra mensaje.
    # def test_primera(self):
    #     mostrar = "tres no es mayor a tres"
    #     self.assertFalse(p1 <= 3, mostrar)

    # si no es verdadero cumple excepcion y muestra mensaje.
    def test_segunda(self):
        mostrar = "no es entero!"
        self.assertEqual(p1, list, mostrar)

    def test_mostrar(self):
        print(p1)

    def test_equal(self):
        mostrar = "no es entero!"
        self.assertEqual(type(p1), int, mostrar)


unittest.main(argv=[""], verbosity=2, exit=False)
test_mostrar(__main__.Probando_excepciones)
test_equal(__main__.Probando_excepciones)
# test_segunda(__main__.Probando_excepciones)
