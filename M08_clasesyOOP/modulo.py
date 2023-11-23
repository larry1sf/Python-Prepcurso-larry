class Transferir:
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
