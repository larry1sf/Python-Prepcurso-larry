#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
hello= 1
print(hello)




# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(hello))



# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre = "larry"


# 5) Crear una variable que contenga un número complejo

# In[3]:

numero_complejo = 3 * 2



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(numero_complejo))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

true = True
false = not True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(false,true)



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 1 + 1.0



# 11) Realizar una operación de suma de números complejos

# In[2]:

a = 2+2
b=3+3
a+b



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
a_1 = 4
b_2=3+3
a_1+b_2


# 13) Realizar una operación de multiplicación

# In[5]:

5*4



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

print(27/4)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
parte_entera = 27//4
print(parte_entera)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
solo_resto = 27%4
print(solo_resto)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

resul = (parte_entera * 4) + solo_resto
print(resul)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

nombre = "larrys"
nombre_completo = nombre+" ceballos"
print(nombre_completo)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

#porque es una cadena de texto
print("2"==2)


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:


print(int("2")==2)


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#porque si llega '' son str no float



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:


resto_contenido = 3
resto_contenido -= 1
print(resto_contenido)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


print(1<<2)
#porque se movio en un sistema binario
#es como multiplicar el numero por 2 y elevarlo el numero de veces movido 
#un sistema para contarque usan las maquinas basados en aunsencia y presencia.

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

#z = 2 + '2'
#porque son dos tipos de variables diferentes y no se puede modificar numericamente un string 
#pero si se puede operar por el como sumas o multiplicaciones que repliten el str

#no funcionaria.
#print(z)


# 26) Realizar una operación válida entre valores de tipo entero y string

#In[30]:
iss= "ssssss"
oss= "aaaa"
operacion= iss * 4
print("i"+ operacion +' hpt'+ oss * 4)
