numeros = 5
#el ciclo for funciona iterando una variable que creamos

# for i in numeros:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print('no es par')
#el ciclo while funciona si una condicion es verdadera
# numero_seis= 5
# if type(numero_seis)==int:
#     if numero_seis > 0:
#         factorizacion = numero_seis
#         while numero_seis > 2:
#             numero_seis -= 1
#             factorizacion = factorizacion* numero_seis
#         print(f'el factorial es {factorizacion}')
#     else:print('no es mayor a cero')
# else:print('no es un entero')
 
 
 # continue+
calcu = []
while numeros > 0:
    numeros -= 1
    if numeros == 1:
        continue
    print(numeros)