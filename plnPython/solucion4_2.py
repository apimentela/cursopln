# -*- coding: utf-8 -*-

'''
El ejercicio consiste en meter dentro de una lista fragmentos de texto, usando como separador las líneas VACÍAS
'''

carpeta_nombre="Documentos\\"
archivo_nombre="DOF_P_IFT_291116_672_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

parrafo=""
parrafos_lista=[]
for linea in lineas_lista:
	if linea.strip() == "":
		if parrafo != "":
			parrafos_lista.append(parrafo)
		parrafo=""
	else:
		parrafo+=linea
if parrafo!="":
	parrafos_lista.append(parrafo)

# EN ESTE PUNTO, LA SOLUCIÓN ESTÁ EN parrafos_lista
