"""
	Problema_1
	Laboratorio 1
	autor: drmorales4
"""

horas = input("Ingrese el numero de horas trabajadas: ") # ingreso de datos de las horas trabajadas

costo = input("Ingrese el costo por cada hora trabajada: ") # ingreso de datos del costo de cada hora trabajada

sueldo = float (horas) * float (costo) # sacando el sueldo original sin el descuento

descuento = float (sueldo) * 0.10  # sacando el descuento del 10% al sueldo original
sueldoPagar = float (sueldo) - float (descuento)  # el valor del suelto fial, restando el sueldo original menos que descuento del 10 %

print("\nEl sueldo base (sin descuento) es: %.2f \nUn descuento de: %.2f \nEl sueldo a pagar es: %.2f" % (sueldo, descuento, sueldoPagar) )
# imprimiendo en pantalla el sueldo a pagar a ese trabajador y el descuento que hubo
