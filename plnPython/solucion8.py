# -*- coding: utf-8 -*-

'''
El ejercicio consiste en repetir el ejercicio anterior usando final del texto en lugar de inicio
'''

import re

carpeta_nombre="Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

expresion_regular=re.compile(r".$")

for linea in lineas_lista:
	resultado_busqueda=expresion_regular.search(linea)
	if resultado_busqueda:
		print(resultado_busqueda.group(0))
