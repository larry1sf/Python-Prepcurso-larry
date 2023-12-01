#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:
import sys

# In[2]
sys.path.append(r"D:\vs\prepcuso\Python-Prepcurso-larry\M08_clasesyOOP")
# print(sys.path)
import modulo as m


# In[3]
# prueba = m.Transferir("texto")
# In[4]
prueba = m.Transferir([1, 2, 3, 4, 5])

# prueba.es_primo()
# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:
# prueba = m.Transferir([21, 22, 23, 24, 25])
# prueba.convertir("farenheit", "kelvin")
# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# ""
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

import unittest


class Probrando_clase(unittest.TestCase):
    def test_primer_caso(self):
        aviso = "error"
        self.assertRaises(ValueError, m.Transferir, aviso)

    def test_segundo_caso(self):
        self.assertEqual(m.Transferir, m.Transferir, "no tan error")

    def test_tercer_caso(self):
        lis = [1, 2, 1, 3]
        p1 = m.Transferir(lis)
        moda, repe = p1.mas_repetido(False)
        moda = [moda]
        moda.append(repe)
        mostrar = [1, 2]
        self.assertTrue(moda == mostrar, "hola!")


# In[9]
# unittest.main(argv=[""], verbosity=2, exit=False)

# test_primer_caso(__main__.Probrando_clase)
# test_segundo_caso(__main__.Probrando_clase)
# test_tercer_caso(__main__.Probrando_clase)


# 4) Probar una creación incorrecta y visualizar la salida del "raise"


# In[13]:
# h2 = m.Transferir("hl")

# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo


# In[14]:
class Caso_primo(unittest.TestCase):
    def test_verifica_primo(self):
        lis = [5, 6, 7, 8, 9]
        h2 = m.Transferir(lis)
        primos = h2.es_primo()
        resul = [True, False, True, False, False]
        self.assertEqual(primos, resul)


# 7) Agregar casos de pruebas para el método conversion_grados()

import importlib

importlib.reload(m)


class Caso_conversion(unittest.TestCase):
    def test_coversion(self):
        lis = [1, 2, 3, 4, 5, 1]
        h3 = m.Transferir(lis)
        grados = h3.convertir("celsius", "farenheit")
        posibles = [33.8, 35.6, 37.4, 39.2, 41.0, 33.8]
        self.assertEqual(grados, posibles)


# In[17]:


# 8) Agregar casos de pruebas para el método factorial()


# In[20]:
class Caso_factorial(unittest.TestCase):
    def test_factorial(self):
        lis = [12, 13, 14, 15, 16]
        h1 = m.Transferir(lis)
        b = h1.factorial()
        factores = [479001600, 6227020800, 87178291200, 1307674368000, 20922789888000]
        self.assertEqual(b, factores)


unittest.main(argv=[""], verbosity=2, exit=False)
test_factorial(__main__.Caso_factorial)
