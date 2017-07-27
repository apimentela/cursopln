carpeta_nombre="/home/alejandro/Escritorio/PaginaCurso/presentacion/Documentos/"
archivo_nombre="P_IFT_290216_73_Acc.txt"

import os
import re
import nltk

#~ carpeta_nombre="C:\\Users\\user\\Desktop\\Documentos\\"
archivo_nombre="P_IFT_290216_73_Acc.txt"
#~ archivo_nombre="COMPENDIO.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()
	
palabras_funcionales=nltk.corpus.stopwords.words("spanish")

tokens=nltk.word_tokenize(texto,"spanish")

tokens_limpios=[]
for token in tokens:
	if token not in palabras_funcionales:
		if len(token) > 1:
			tokens_limpios.append(token)

texto_limpio_nltk=nltk.Text(tokens_limpios)

from nltk.tag import StanfordPOSTagger

# Aquí obtenemos la lista de tokens en "tokens"

texto_nltk=nltk.Text(tokens)

tagger="C:\\Users\\user\\Downloads\\...\\spanish.tagger"
jar="C:\\Users\\user\\Downloads\\...\\stanford-postagger.jar"

etiquetador=StanfordPOSTagger(tagger,jar)
etiquetas=etiquetador.tag(tokens)

for etiqueta in etiquetas:
	print(etiqueta)
