# -*- coding: utf-8 -*-

import os
import re

carpeta_nombre="Descargas\\"

archivos_lista=os.listdir(carpeta_nombre)

expresion_regular=re.compile(r"\.docx?$")

for archivo_nombre in archivos_lista:
	resultado_busqueda=expresion_regular.search(archivo_nombre)
	if resultado_busqueda:
		print(resultado.group(0))
