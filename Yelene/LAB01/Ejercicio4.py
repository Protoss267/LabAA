import matplotlib.pyplot
import pandas

dic = {"ciudades": ["Zaragoza", "Valladolid", "Moscu", "Toronto", "Caracas"],
    "poblacion": [5597349, 10941249, 26789397, 19465357, 8967183],
    "pais": ["Espanna", "Espanna", "Rusia", "Canada", "Venezuela"]}

tb = pandas.DataFrame(dic)
tb.plot.bar(x='ciudades', y='poblacion')
matplotlib.pyplot.xlabel("Ciudades")
matplotlib.pyplot.ylabel("Poblacion")
matplotlib.pyplot.title("Poblaciones")
matplotlib.pyplot.show()