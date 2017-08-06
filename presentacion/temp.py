carpeta_nombre="/home/alejandro/cursopln/presentacion/Documentos/"
archivo_nombre="P_IFT_290216_73_Acc.txt"

import os
import re
import nltk

#~ carpeta_nombre="C:\\Users\\user\\Desktop\\Documentos\\"
#~ archivo_nombre="Legales/DOF_P_IFT_290216_71_Datos_Relevantes_Acc.txt"
archivo_nombre="DOF_P_IFT_291116_672_Acc.txt"
#~ archivo_nombre="COMPENDIO.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	lineas_lista=archivo.readlines()

num_linea=1
for linea in lineas_lista:
	linea=linea.strip()
	if linea == "":
		continue
	print("LINEA",num_linea,":",linea)
	num_linea=num_linea+1
	
#~ for linea in lineas_lista:
	#~ print("LINEA",num_linea,":",linea)
	#~ num_linea=num_linea+1


	
#~ palabras_funcionales=nltk.corpus.stopwords.words("spanish")

#~ tokens=nltk.word_tokenize(texto,"spanish")
#~ texto_nltk=nltk.Text(tokens)
#~ texto_nltk.similar("artículo")
#~ print()
#~ texto_nltk.common_contexts(["artículo","instituto"])

#~ lista_palabras=["Instituto","Ley","Elija","ley"]
#~ texto_nltk.dispersion_plot(lista_palabras)


#~ tokens_limpios=[]
#~ for token in tokens:
	#~ if token not in palabras_funcionales:
		#~ if len(token) > 1:
			#~ tokens_limpios.append(token)

#~ texto_limpio_nltk=nltk.Text(tokens_limpios)

#~ from nltk.tag import StanfordPOSTagger

#~ # Aquí obtenemos la lista de tokens en "tokens"

#~ texto_nltk=nltk.Text(tokens)

#~ tagger="C:\\Users\\user\\Downloads\\...\\spanish.tagger"
#~ jar="C:\\Users\\user\\Downloads\\...\\stanford-postagger.jar"

#~ etiquetador=StanfordPOSTagger(tagger,jar)
#~ etiquetas=etiquetador.tag(tokens)

#~ for etiqueta in etiquetas:
	#~ print(etiqueta)
