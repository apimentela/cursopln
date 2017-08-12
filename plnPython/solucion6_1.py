# -*- coding: utf-8 -*-

carpeta_nombre="Solucion5\\"
archivo_nombre="UNION.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
	texto=texto.replace(simbolo," " + simbolo + " ")

palabras_lista=texto.split()

palabras_unicas=[]

for palabra in palabras_lista:
	if palabra in palabras_unicas:
		continue
	palabras_unicas.append(palabra)

# EN ESTE PUNTO LA SOLUCIÓN ESTÁ EN palabras_unicas
