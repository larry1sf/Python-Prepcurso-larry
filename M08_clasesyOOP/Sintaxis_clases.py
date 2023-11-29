# se declara de la siguiente manera :
class Auto:
    #declaramos el metodo constructor
    def __init__(self,nombre,edad,tipo,estilo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.estilo = estilo
#metodo presentar 
    def presentar (self):
        return print('Nombre:',self.nombre,' Edad:',self.edad,'años',' Tipo de carro:',self.tipo,' Estilo:',self.estilo)
#herencia
carro = Auto('Ferrari',20,'auto','Deportivo')
#muestra la posicion del objeto. de la clase Auto.
print(carro)
#muestra el contenido del objeto
carro.presentar()
#instanciamos la herencia de la clase padre auto y le asignamos valores nuevos.
carro2 = Auto('chebrolet',25,'auto','Deportivo')
carro2.presentar()

# se pueden mostrar elementos por separado de dicha asignacion.
class Animal:
    def __init__(self,raza,edad,color):
        self.raza = raza 
        self.edad = edad
        self.color = color

    def me_presento(self):
        return print('Hola, soy',self.raza,'y tengo',self.edad,'años y soy',self.color)

    def cumpli(self):
        self.edad += 1

a1 = Animal('perro',4,'negro')
a2 = Animal('Gato',3,'blanco')

print(a1.raza)
print(a1.edad)
print(a1.color)

print(a2.raza)
print(a2.edad)
print(a2.color)

a1.me_presento()
a2.me_presento()

a2.cumpli()
a2.cumpli()


a1.me_presento()
a2.me_presento()

class Personita:
    def __init__(self,nombre,edad,color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def me_presento(self):
        return print(f'tienes {self.edad}años y eres {self.color} tu nombre sera {self.nombre}')
    def me_presento(self,larry):
        return print(f'hola {larry} eres {self.color} verdad, y tienes {self.edad}años al parecer')
p1= Personita('larry',29,'negro')
p1.me_presento()