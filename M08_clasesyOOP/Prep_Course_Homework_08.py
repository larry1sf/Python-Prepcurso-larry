#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor


# In[1]:
class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje


# vehiculo1 = Vehiculo(color, tipo, cilindraje)


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>


# In[5]:
class Vehiculo:
    def __init__(
        self,
        color,
        tipo,
        cilindraje,
    ):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = ""

    def acelera(self, vel):
        self.velocidad += vel

    def frena(self, vel_frenada):
        self.velocidad -= vel_frenada

    def dobla(self, direccion):
        self.direccion = direccion


# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
vehiculo1 = Vehiculo("red", "auto", "medio")
vehiculo2 = Vehiculo("blue", "moto", "alto")
vehiculo3 = Vehiculo("gris", "camion", "bajo")
# In[7]
vehiculo2.acelera(120)
vehiculo2.acelera(20)
vehiculo2.acelera(10)
vehiculo2.frena(100)
vehiculo2.dobla("derecha")
vehiculo2.dobla("izquierda")
vehiculo2.dobla("izquierda")

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada


# In[12]:
class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = ""

    def acelera(self, vel):
        self.velocidad += vel

    def frena(self, vel_frenada):
        self.velocidad -= vel_frenada

    def dobla(self, direccion):
        self.direccion = direccion

    def estado(self):
        print(
            f"vas a {self.velocidad} kilometos por hora, y  vas mirando hacia {self.direccion}"
        )

    def mirar_tipo(self):
        print(
            "El color es: ",
            self.color,
            "El tipo de vehiculo es: ",
            self.tipo,
            "El cilindraje es: ",
            self.cilindraje,
        )


# In[13]:

vehiculo1 = Vehiculo("azul", "moto", "alto")
vehiculo1.acelera(120)
vehiculo1.frena(40)
vehiculo1.dobla("derecha")
# In[14]
# vehiculo1.mirar_tipo()

# vehiculo1.estado()


# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>


# In[33]:
class Verificacion_de:
    def __init__(self):
        pass

    # metodo de numero primo
    def es_primo(self, n):
        for i in range(2, n):
            if (n % i) == 0:
                return print(not True)
        return print(not False)

    # metodo de valor modal
    def mas_repetido(self, lista_numeros):
        lista_repeticiones = []
        lista_unicos = []
        if len(lista_numeros) == 0:
            return None
        for u in lista_numeros:
            if u in lista_unicos:
                i = lista_unicos.index(u)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(u)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, u in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return print(f"el valor modal es {moda}, y se repite {maximo} veces")

    # metodo de conversion de grados
    def convertir(self, valor, origen, medida_salida):
        """es farenheit cuando"""
        valor_farenhait = (valor * 9 / 5) + 32
        """es kelvin cuando"""
        valor_kelvin = valor + 273.15
        if origen == "celsius":
            if medida_salida == "celsius":
                return print(valor)
            elif medida_salida == "farenheit":
                return print(valor_farenhait)
            elif medida_salida == "kelvin":
                return print(valor_kelvin)
            else:
                return print("parametro de destino incorrecto")
        elif origen == "farenheit":
            if medida_salida == "farenheit":
                return print(valor)
            elif medida_salida == "celsius":
                return print((valor - 32) * 9 / 5)
            elif medida_salida == "kelvin":
                return print((valor - 32) * 9 / 5 + 273.15)
            else:
                return "parametro de destino incorrecto"
        elif origen == "kelvin":
            if medida_salida == "kelvin":
                return print(valor)
            elif medida_salida == "farenheit":
                return print((valor + 273.15) * 9 / 5)
            elif medida_salida == "celsius":
                return print(valor - 273.15)
            else:
                return print("el parametro de destino es incorrecto")
        else:
            return print("el parametro de origen es incorrecto")

    # metodo factorial
    # reparar
    def factorial(self, numero):
        numero -= 1
        if type(numero) != int:
            return print("El numero debe ser un entero")
        if numero > 1:
            return numero * self.__factorial(numero - 1)
        else:
            return 1


# 6) Probar las funciones incorporadas en la clase del punto 5
prueba = Verificacion_de()

# In[28]:
# prueba.es_primo(5)
# prueba.mas_repetido([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3])
# prueba.convertir(4, "celsius", "kelvin")
# reparar
# print(prueba.factorial(4))
# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas


# In[55]:
class Verificacion_de:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    # metodo de numero primo
    def es_primo(self):
        for i in self.lista:
            if self.__es_primo(i):
                print("el elemento", i, "ES un primo")
            else:
                print("el elemento", i, "NO es un primo")

    def __es_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    # metodo de valor modal
    def mas_repetido(self, lista_numeros):
        lista_repeticiones = []
        lista_unicos = []
        if len(self.lista) == 0:
            return None
        if lista_numeros:
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for u in self.lista:
            if u in lista_unicos:
                i = lista_unicos.index(u)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(u)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, u in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    # metodo de conversion de grados
    def convertir(self, origen, destino):
        for i in self.lista:
            print(
                i,
                "grados",
                origen,
                "son",
                self.__convertir(i, origen, destino),
                "grados",
                destino,
            )

    def __convertir(self, valor, origen, medida_salida):
        valor_destino = None
        """es farenheit cuando"""
        valor_farenhait = (valor * 9 / 5) + 32
        """es kelvin cuando"""
        valor_kelvin = valor + 273.15

        if origen == "celsius":
            if medida_salida == "celsius":
                valor_destino = valor
            elif medida_salida == "farenheit":
                valor_destino = valor_farenhait
            elif medida_salida == "kelbin":
                valor_destino = valor_kelvin
            else:
                print("parametro de destino incorrecto")

        elif origen == "farenheit":
            if medida_salida == "farenheit":
                valor_destino = valor
            elif medida_salida == "celsius":
                valor_destino = (valor - 32) * 5 / 9
            elif medida_salida == "kelvin":
                valor_destino = (valor - 32) * 5 / 9 + 273.15
            else:
                print("parametro de destino incorrecto")

        elif origen == "kelvin":
            if medida_salida == "kelvin":
                valor_destino = print(valor)
            elif medida_salida == "farenheit":
                valor_destino = (valor - 273.15) * 9 / 5 + 32
            elif medida_salida == "celsius":
                valor_destino = valor - 273.15
            else:
                print("el parametro de destino es incorrecto")
        else:
            print("el parametro de origen es incorrecto")
        return valor_destino

    # metodo factorial
    def factorial(self):
        for i in self.lista:
            print("el factorial de ", i, "es ", self.__factorial(i))

    # metodo factorial
    def __factorial(self, n):
        if n > 1:
            return n * self.__factorial(n - 1)
        else:
            return 1


prueba = Verificacion_de([1, 1, 2, 5, 8, 8, 9, 11, 15, 16, 16, 16, 18, 20])
# prueba.es_primo()
# moda, repe = prueba.mas_repetido(False)
# print(moda, repe)
# moda, repe = h.valor_modal(False)
# prueba.convertir("celsius", "farenheit")
# prueba.factorial()
# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

from modulo import Transferir

# In[2]
h = Transferir([1, 2, 2, 2, 5, 8, 8, 9, 11, 15, 16, 16, 16, 18, 20])

# h.es_primo()
# m, r = h.mas_repetido(True)
# print("Mas: ", m, "Repetido:", r)
# h.convertir("farenheit", "celsius")
# h.factorial()
