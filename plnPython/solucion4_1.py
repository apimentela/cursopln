# -*- coding: utf-8 -*-

'''
El ejercicio consiste en mostrar el contenido de un archivo del inicio hasta la primer línea vacía.
'''

carpeta_nombre="Documentos\\"
archivo_nombre="DOF_P_IFT_291116_672_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

for linea in lineas_lista:
	if linea.strip() == "":
		break
	print(linea)
