# Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas, horarios o marcas de tiempo se puede utilizar la clase datetime

import datetime

# muestra todo el conjunto de fecha mes y hora con un sub conjunto de  numers byte por mili segundos.
tiempo_ahor = datetime.datetime.now()

# pasa la fecha escrita pero no la  hora
fecha_fija = datetime.datetime(2023, 11, 30)


# devuelve el string  la feha y hora sesignada para usar timestamp()
fecha_hora = "2023-11-30 15:30:00"
objeto_datetime = datetime.datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S")


# da como un numero float marcado de timestamp() para usar en fromtimestamp()
marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)

# nos da la hora que le metimos.
fecha_hora_2 = datetime.datetime.fromtimestamp(tiempo_ahor)
print("ejp  fromtimestamp=", fecha_hora_2)
