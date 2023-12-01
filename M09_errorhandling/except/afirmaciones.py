def saca_primera_letra(lista):
    lista_vacia = []
    for i in lista:
        assert type(i) == str, f"{i} no es un string"
        assert len(i) > 0, f"No se admiten menores a 0"
        lista_vacia.append(i[0])
    return lista_vacia


palabritas = ["jose", "hino", 2]
saca_primera_letra(palabritas)


##ASSERT (BOOLEANO),(MENSAJE A MOSTRAR COMO EXCEPT)
