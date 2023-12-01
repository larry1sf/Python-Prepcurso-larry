import sys
import datetime


temperatura = input("introduce el valor de la temperatura: ")
humedad = input("introduce el valor de la humedad: ")
llovio = sys.argv[1]


fecha = "2023-11-30-16:18:00"
obj_dt = datetime.datetime.strptime(fecha, "%Y-%m-%d-%H:%M:%S")
marca_de_tiempo = datetime.datetime.timestamp(obj_dt)
linea_agregar = f"{marca_de_tiempo},{temperatura},{humedad},{llovio}"

ar = open("clase09_ej2_larry.csv", "a")
ar.write(linea_agregar + "\n")
ar.close()
