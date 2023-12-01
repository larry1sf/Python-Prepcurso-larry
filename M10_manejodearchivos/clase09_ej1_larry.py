import sys

print(f"{sys.argv[0]}")
if len(sys.argv) == 4:
    salida = sys.argv[1:]
    [print(f"el parametro numero {salida.index(i)+1} es {i}") for i in salida]
else:
    raise ValueError(
        "Introduciste (1) , (2) o mas argumentos" + "\n"
        "ERROR... introduce los argumentos correctamente"
    )
