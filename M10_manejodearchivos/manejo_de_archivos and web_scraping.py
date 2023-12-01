import os

# mejor manejo de archivos y web scrapping
lis = ["larry", "sonia", "dora"]
# escritura
# archivo = open("nuevo_1.txt", "w")
# for i in lis:
#     archivo.write(i + "\n")
# archivo.close()
# lectura
# leer = open("nuevo_1.txt", "r")
# for i in leer:
# print(i)
# leer.close()


from bs4 import BeautifulSoup
import urllib.request

# instanciamos el link de la pagina y le decimos que lo agrege a una variable para leerla
response = urllib.request.urlopen("https://es.wikipedia.org/wiki/Colombia")
htlm = response.read()
# le asignamos el beutiful con los parametros de la variable leida para que devuelva solo lo que se le asigne. es este caso solo texto.
soup = BeautifulSoup(htlm, "html.parser")
text = soup.get_text()
# en este caso especificamos que solo las etiquetas a(que son para links.)
links = soup.find_all("a")
p = soup.find_all("b")
