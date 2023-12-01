# -*- coding: utf-8 -*-
montañas = {
    "nombre": [
        "Everest",
        "K2",
        "Kanchenjunga",
        "Lhotse",
        "Makalu",
        "Cho Oyu",
        "Dhaulagiri",
        "Manaslu",
        "Nanga Parbat",
        "Annapurna I",
    ],
    "orden": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "cordillera": [
        "Himalaya",
        "Karakórum",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Himalaya",
        "Karakórum",
        "Himalaya",
    ],
    "pais": [
        "Nepal",
        "Pakistán",
        "Nepal",
        "Nepal",
        "Nepal",
        "Nepal",
        "Nepal",
        "Nepal",
        "Pakistán",
        "Nepal",
    ],
    "altura": [8849, 8611, 8586, 8516, 8485, 8188, 8167, 8163, 8125, 8091],
}

ar = open("clase09_ej3_larry.csv", "a")
for i in montañas.keys():
    if i == "altura":
        ar.write(i + "\n")
    else:
        ar.write(i + ",")

ond = 0
while ond < 10:
    ar.write(str(montañas["nombre"][ond]) + ",")
    ar.write(str(montañas["orden"][ond]) + ",")
    ar.write(str(montañas["cordillera"][ond]) + ",")
    ar.write(str(montañas["pais"][ond]) + ",")
    ar.write(str(montañas["altura"][ond]) + ",\n")
    ond += 1
ar.close()
