activo = True
listado = []


class Cliente:
    def __init__(self, nombre, numero, info, talla):
        self.nombre = nombre
        self.__numero = numero
        self.__info = info
        self.__talla = talla

    def informar(self):
        print(
            "\n                                             Nombre:",
            self.nombre,
            "\n                                             Numero:",
            self.__numero,
            "\n                                             Informacion:",
            self.__info,
            "\n                                             Talla:",
            self.__talla,
        )


def pedida():
    nombre = str(input("nombre:  "))
    numero = input("numero:  ")
    info = str(input("info:  "))
    talla = input("Talla:   ")
    return nombre, numero, info, talla


def pregunta():
    entrada = str(input("Quieres añadir otro? "))
    while entrada != "n" and entrada != "y":
        entrada = str(input("Quieres añadir otro?   "))
    if entrada == "y":
        return True
    if entrada == "n":
        return not True


def meter_cliente(n, nu, i, t):
    x = Cliente(n, nu, i, t)
    listado.append(x)
    print(listado)


def cuerpo(T):
    if T == True:
        abrir(activo)
    else:
        print("estas en un punto muerto")
        for i in listado:
            i.informar()


def abrir(activo):
    while activo:
        n, nu, i, t = pedida()
        meter_cliente(n, nu, i, t)
        r = pregunta()
        cuerpo(r)
        activo = False


# abrir(activo)


# agregando con el metodo super..
# las propiedades de un padre a c_mayor como clase hija..
# y añadi otra propiedad extra que se tiene que mostrar en
# un metodo aparte ya que no  hace parte de una clase hija..
class C_mayor(Cliente):
    def __init__(self, nombre, numero, info, talla, otra):
        super().__init__(nombre, numero, info, talla)
        self.otra = otra

    def print(self):
        print(self.otra)


q, w, e, r = pedida()
hijo_c = C_mayor(q, w, e, r, 0)

hijo_c.print()
