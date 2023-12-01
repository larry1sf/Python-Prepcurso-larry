class Transferir:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
        if type(lista_numeros) != list:
            self.lista = []
            raise ValueError(f"el parametro esta recibiendo un valor que no es lista")
        else:
            self.lista = lista_numeros

    # metodo de numero primo
    def es_primo(self):
        lis_resul = []
        for i in self.lista:
            if self.__es_primo(i):
                lis_resul.append(True)
            else:
                lis_resul.append(False)
        return lis_resul

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
        parametros_entrada = ["celsius", "farenheit", "kelvin"]
        lista_conversion = []
        if origen not in parametros_entrada:
            print("los parametros esperados eran", parametros_entrada)
            return lista_conversion
        if destino not in parametros_entrada:
            print("los parametros esperados eran", parametros_entrada)
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__convertir(i, origen, destino))
        return lista_conversion

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
            elif medida_salida == "kelvin":
                valor_destino = valor_kelvin
            else:
                valor_destino = valor + 273.15

        elif origen == "farenheit":
            if medida_salida == "farenheit":
                valor_destino = valor
            elif medida_salida == "celsius":
                valor_destino = (valor - 32) * 5 / 9
            elif medida_salida == "kelvin":
                valor_destino = (valor - 32) * 5 / 9 + 273.15
            else:
                valor_destino = ((valor - 32) * 5 / 9) + 273.15

        else:
            if medida_salida == "farenheit":
                valor_destino = (valor - 273.15) * 9 / 5 + 32
            elif medida_salida == "celsius":
                valor_destino = valor - 273.15
            else:
                valor_destino = valor
        return valor_destino

    # metodo factorial
    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial

    # metodo factorial
    def __factorial(self, n):
        if n > 1:
            return n * self.__factorial(n - 1)
        else:
            return 1
