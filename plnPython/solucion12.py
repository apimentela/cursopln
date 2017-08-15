# -*- coding: utf-8 -*-

import re

carpeta_nombre="Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

expresion_regular=re.compile(r"artículos? \d+(, \d+)*( y \d+)*")
resultado_busqueda=expresion_regular.finditer(texto)
for resultado in resultado_busqueda:
	print(resultado.group(0))
