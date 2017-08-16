# -*- coding: utf-8 -*-

'''
El ejercicio consiste en extraer las fechas de un documento, se toman en cuenta fechas como: 13 de agosto del 2017
'''

import re

carpeta_nombre="Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"

meses=r"([Ee]nero|[Ff]ebrero|[Mm]arzo|[Aa]bril|[Mm]ayo|[Jj]unio|[Jj]ulio|[Aa]gosto|[Ss]eptiembre|[Oo]ctubre|[Nn]oviembre|[Dd]iciembre)"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

expresion_regular=re.compile(r"\d+\sde\s"+meses+r"\sdel?\s\d+")
resultado_busqueda=expresion_regular.finditer(texto)
for resultado in resultado_busqueda:
	print(resultado.group(0))
