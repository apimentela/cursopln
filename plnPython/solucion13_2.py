# -*- coding: utf-8 -*-

'''
El ejercicio consiste en extraer las fechas escritas con letras
'''

import re

carpeta_nombre="Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"

meses=r"([Ee]nero|[Ff]ebrero|[Mm]arzo|[Aa]bril|[Mm]ayo|[Jj]unio|[Jj]ulio|[Aa]gosto|[Ss]eptiembre|[Oo]ctubre|[Nn]oviembre|[Dd]iciembre)"
numeros=r"(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieci|veinte|veinti|treinta|treinti|cuarenta|cuarenti|cincuenta|cincuentai|sesenta|sesentai|setenta|setentai|ochenta|ochentai|noventa|noventai|cien|ciento|cientos|quinientos|nove|mil|\s)+"
ordinales=r"(primero|segundo|tercero|cuarto|quinto|sexto|séptimo|octavo|noveno|décimo|undécimo|duodécimo|vigésimo|trigésimo|\s)+"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

expresion_regular=re.compile(ordinales+"de\s"+meses+"\sdel?"+numeros)
resultado_busqueda=expresion_regular.finditer(texto)
for resultado in resultado_busqueda:
	print(resultado.group(0))

# En esta solución se muestra cómo obtener únicamente las fechas que usan letras, el anterior muestra cómo obtener los números, para ambos se pueden usar los dos procesos uno tras otro, o bien con una expresión regular que una las dos expresiones con la instrucción de opción: |
