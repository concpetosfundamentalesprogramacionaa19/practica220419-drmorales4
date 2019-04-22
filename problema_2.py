"""
	Problema_2
	Laboratorio 1
	autor: drmorales4
"""

x = input("Por favor Ingrese X valor: ") # ingresando valor de x
y = input("Por favor Ingrese Y valor: ") #ingresando valor de y
z = input("Por favor Ingrese Z valor: ") # ingresando valor de z



valorx = float(x) # conversion de cadena de texto a decimal el valor de x
valory = float(y) # conversion de cadena de texto a decimal el valor de y
valorz = float(z) # conversion de cadena de texto a decimal el valor de z

m = (valorx+(valory/valorz))/(valorx-(valory/valorz)) # realizando la operacion segun la formula pedida

# presentacion en pantalla de los valores de x, y, z, y tambien del valor de "m"

print("El valor de m, en base a las variables: \nx= %.1f \n\ty= %.1f \n\t\tz= %.1f \nda como resuldo: \n\t\t m= %.1f" % (valorx, valory, valorz, m) )