import numpy as np
import pandas as pd
import matplotlib.pyplot as mt
######################Ejercicio 1#########################
x = np.arange(1, 10, 1)
a = x.reshape([3, 3])
print(a)
print("Fin del ejercicio 1")


######################Ejercicio 2##########################
a = np.zeros([5, 3], dtype=int)
print(a)
print("Fin del ejercicio 2")

######################Ejercicio 3##########################
diccionario = {
    "ciudades": ["Matanza", "La Habana", "Pinar del Rio", "Alaska", "Iowa"],
    "poblacion": [1654296, 2467853, 559123, 1765240, 5123961],
    "pais": ["Cuba", "Cuba", "Cuba", "Yuma", "Yuma"]
}
DF_diccionario = pd.DataFrame(diccionario)
print("DATAFRAME CREADO\n",DF_diccionario, end="\n")
pais = input("diga el pais\n")
DF_diccionario_pais = DF_diccionario.query("pais ==@pais")
print("Filtrado de paises\n",DF_diccionario_pais, end="\n")
DF_mas_500000 = DF_diccionario[DF_diccionario['poblacion']> 500000].shape[0]
print("Cantidad de paises con mas de 500000\n",DF_mas_500000, end="\n")
print("Fin del ejercicio 3")
######################Ejercicio 4##########################
DF_diccionario.plot.bar(x='ciudades', y='poblacion')
mt.xlabel("Ciudad")
mt.ylabel("Poblacion")
mt.title("Poblacion de ciudades")
mt.show()
print("Fin del ejercicio 4")
######################Ejercicio 5##########################
x = np.linspace(-5, 5, 100)
y= np.tan(x)
mt.plot(x,y)
mt.xlabel("x")
mt.ylabel("tan(x)")
mt.title("Grafico de la tangente")
mt.show()
print("Fin del ejercicio 5")