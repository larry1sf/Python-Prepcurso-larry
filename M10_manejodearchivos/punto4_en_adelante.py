# 4) Mostrar el tamaño en MB del archivo generado en el punto 3
import os

bts = os.path.getsize("clase09_ej3_resull_larry.csv")


print(str(bts / 1000) + " MB")

# 5) Crear una carpeta llamada clase09_montañas_altas

# os.makedirs("clase09_montañas_bajas")

# 6) Copiar el archivo clase09_ej3.scv en la carpeta clase09_montañas_altas usando la sentencia **os.system**


# os.system("copy clase09_ej3_resul_larry.csv clase09_montañas_bajas")

# 7) Listar el contenido de la carpeta clase09_montañas_altas

print("el contenido de la lista es", os.listdir("./clase09_montañas_bajas"))
