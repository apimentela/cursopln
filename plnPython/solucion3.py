# -*- coding: utf-8 -*-

'''
El ejercicio consiste en en:
- Contar las líneas que tiene un archivo y mostrar el número junto a cada línea
- Mostrar el contenido de cada línea, y en caso de que esté vacía, indicar en pantalla que la línea esta vacía.
- Mostrar en pantalla un conteo final indicando cuántas líneas son en total, cuántas tienen texto y cuántas no.
'''

carpeta_nombre="Documentos\\"
archivo_nombre="DOF_P_IFT_291116_672_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

num_linea=1
num_texto=0
num_vacio=0
for linea in lineas_lista:
	if linea.strip() == "":
		num_linea=num_linea+1
		print("LINEA",num_linea,":","Esta línea está vacía")
		num_vacio=num_vacio+1
	else:
		num_linea=num_linea+1
		print("LINEA",num_linea,":",linea)
		num_texto=num_texto+1

print("Lineas totales:",num_linea)
print("Lineas con texto:",num_texto)
print("Lineas vacías:",num_vacio)

# OTRA FORMA DE RESOLVERLO:

lista_texto=[]
lista_vacio=[]
for linea in lineas_lista:
	if linea.strip() == "":
		print("LINEA",num_linea,":","Esta línea está vacía")
		lista_vacio.append(linea)
	else:
		print("LINEA",num_linea,":",linea)
		lista_texto.append(linea)

print("Lineas totales:",len(lista_texto)+len(lista_vacio))
print("Lineas con texto:",len(lista_texto))
print("Lineas vacías:",len(lista_vacio))
