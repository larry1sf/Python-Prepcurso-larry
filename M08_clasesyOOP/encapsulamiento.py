class Cuenta_Bancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("no tienes fondos suficientes.")

    def inspeccionar(self):
        return print(self.__saldo)


# c1= Cuenta_Bancaria(20000)
#
# c1.inspeccionar()
# c1.retirar(18000)
# c1.inspeccionar()

# class M
