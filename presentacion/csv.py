import csv

# En esta sección se declaran los diccionarios.

with open("frecuencias.csv","w") as archivo_csv:
	escritor_csv = csv.writer(archivo_csv)
	for termino in diccionario_frecuencias["texto1.txt"]:
		escritor_csv.writerow()
