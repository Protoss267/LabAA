import pandas

dic = {"ciudades": ["Zaragoza", "Valladolid", "Moscu", "Toronto", "Caracas"],
    "poblacion": [5597349, 10941249, 26789397, 19465357, 8967183],
    "pais": ["Espanna", "Espanna", "Rusia", "Canada", "Venezuela"]}
tb = pandas.DataFrame(dic)
print(tb, end="\n")

tbPais = dic.query("pais ==Espanna")
print(tbPais, end="\n")
tb500mil = dic[dic['poblacion']> 500000].shape[0]
print(tb500mil, end="\n")