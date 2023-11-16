#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
ejercicio_uno = 1
if ejercicio_uno > 0:
    print('mayor a cero')
else:print('menor a cero')




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

ejercicio_dos = 3
ejercicio_dos_1 = "e"
if type(ejercicio_dos) == type(ejercicio_dos_1):
    print('son del mismo tipo')
else:print('no son del mismo tipo')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

# for i in range(1,21):
#     if i % 2 == 0:
#         print('el numero',str(i),'es par')
#     else:print('el numero',str(i),'no e es par')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

# for i in range(0,5):
    
#     print('el resultado de',i,' numero elevadoa la potencia igual a 3 es',i**3)



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:


# for i in range(1,9):
#     print('llevo el',i,'recorrido')


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
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
    




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

# condicion = True
# while condicion is True:
#     for i in str(condicion):
#         print(i)
#         condicion =  not True



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
# in3= 'True'
# for i in in3:
#     print(type(i))
#     print(type(in3))
#     while type(i) == type(in3):
#         print('se')
#         in3 = False



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
# num_tope= 30
# num= 0
# primo= True
# while num < num_tope:
#     for i in range(2,num):
#         if (num % i==0):
#             primo = False
#         if(primo):
#             print(num)
#         else:primo = True
#     num+=1
# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

# num_tope= 30
# num= 0
# primo= True
# while num < num_tope:
#     for i in range(2,num):
#         if (num % i==0):
#             primo = False
#             break
#     if(primo):
#             print(num)
#     else:
#         primo = True
#     num+=1


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

# num_tope= 30
# cantidad_optimizada = 0
# num= 0
# primo= True
# while num < num_tope:
#     for i in range(2,num):
#         cantidad_optimizada += 1
#         if (num % i == 0):
#             primo = False  
#     if(primo):
#         print(num)
#     else:
#         primo = True
#     num+=1
# print(f'cantidad de numeros optimizados {num_tope}')

# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
# rango_numero_tope = 301
# rango_numero = 100

# while rango_numero_tope == 301:
#     for i in range(rango_numero,rango_numero_tope):
#         if i % 12 == 0:
#             print(i)
#     break
# rango_numero_tope + 1



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

# n = 1
# sigue = 1
# primo = True

# while (sigue == 1):
#     for i in range(2,n):
#         if (n % i == 0):
#             primo = False
#             break 
#     if (primo):
#         print(n)
#         print('Desea buscar otro numero primo introduce un numeroprimo ?')
#         if(input() != '1'):
#             print('se finaliza el proceso')
#             break
#     else:
#         primo = True
#     n +=1   



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


rango = 99
while rango <= 300:
    if(rango % 3 == 0) & (rango % 6 == 0):
        print('El numero es :',rango)
        break
    rango += 1


