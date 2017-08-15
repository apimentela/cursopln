# -*- coding: utf-8 -*-

import re

carpeta_nombre="Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for letra in mayusculas:
	expresion_regular=re.compile(letra+r".*?\.")
	resultado_busqueda=expresion_regular.finditer(texto)
	for resultado in resultado_busqueda:
		print(resultado.group(0))
