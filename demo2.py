"""
	demo2.py
	Ejemplo de lenguaje Pyton
	autor: drmorales4
"""
import sys

nombre_archivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]
suma = int (valor1) + int (valor2) # aqui realizo la suma de variables

print("La suma es: %d" % suma)
