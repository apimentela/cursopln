carpeta_nombre="/home/alejandro/Escritorio/PaginaCurso/presentacion/Documentos/"
archivo_nombre="P_IFT_290216_73_Acc.txt"

#~ import os
#~ import re

#~ #carpeta_nombre="C:\\Users\\user\\Desktop\\Documentos\\"
#~ archivo_nombre="P_IFT_290216_73_Acc.txt"

#~ with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	#~ texto=archivo.read()



#~ expresion_regular=re.compile(r".$")
#~ resultado_busqueda=expresion_regular.search(texto)

#~ print(resultado_busqueda.group(0))



#~ expresion_regular=re.compile(r"II*")
#~ resultados_busqueda=expresion_regular.finditer(texto)

#~ for resultado in resultados_busqueda:
	#~ print(resultado.group(0))


carpeta_nombre="/home/alejandro/Escritorio/PaginaCurso/presentacion/Documentos/"
archivo_nombre="P_IFT_290216_73_Acc.txt"

import os
import re
import nltk

#carpeta_nombre="C:\\Users\\user\\Desktop\\Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

texto_nltk=nltk.Text(tokens)
texto_nltk.concordance("artículo")
