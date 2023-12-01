import sys

# sys es una lista que guarda todo la entrada como argumento en la liena de comandos o terminal

# el nombre del archivo seria el primero guardado en sys.argv[]
print(f"el nombre es :{sys.argv[0]}")
# con la entrada del terminal.
print(f"hola {sys.argv[1]}")
##tipo que se le pasa
print(f"hola {type(sys.argv[1])}")
