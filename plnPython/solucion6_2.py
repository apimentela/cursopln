# -*- coding: utf-8 -*-

'''
El ejercicio consiste en clasificar los documentos en ACUERDOS, RESOLUCIONES y OTROS. Para cada grupo se forma su vocabulario y se separan los símbolos y signos de puntuación de las palabras
'''

import os

carpeta_nombre="Documentos\\"

archivos_lista=os.listdir(carpeta_nombre)

acuerdos=""
resoluciones=""
otros=""

for archivo_nombre in archivos_lista:
	with open(carpeta_nombre+archivo_nombre,"r") as archivo:
		texto=archivo.read()
	if "ACUERDO" in texto and "RESOLUCIÓN" not in texto:
		acuerdos+=texto
	elif "RESOLUCIÓN" in texto and "ACUERDO" not in texto:
		resoluciones+=texto
	else:
		otros+=texto

simbolos=["(",")",",",".",";",":","\""]
acuerdos_simbolos=[]
resoluciones_simbolos=[]
otros_simbolos=[]

for texto in [acuerdos,resoluciones,otros]:

for simbolo in simbolos:
	if simbolo in acuerdos:
		acuerdos_simbolos.append(simbolo)
		acuerdos.replace(simbolo,"")
	if simbolo in resoluciones:
		resoluciones_simbolos.append(simbolo)
		resoluciones.replace(simbolo,"")
	if simbolo in otros:
		otros_simbolos.append(simbolo)
		otros.replace(simbolo,"")

acuerdos_lista=acuerdos.split()
resoluciones_lista=resoluciones.split()
otros_lista=resoluciones.split()

acuerdos_unicas=[]
resoluciones_unicas=[]
otros_unicas=[]

for palabra in acuerdos_lista:
	if palabra in acuerdos_unicas:
		continue
	acuerdos_unicas.append(palabra)

for palabra in resoluciones_lista:
	if palabra in resoluciones_unicas:
		continue
	resoluciones_unicas.append(palabra)

for palabra in otros_lista:
	if palabra in otros_unicas:
		continue
	otros_unicas.append(palabra)

# EN ESTE PUNTO LAS LISTAS acuerdos_unicas , resoluciones_unicas Y otros_unicas TIENEN TODAS LAS PALABRAS CLASIFICADAS Y SIN REPETICIONES
# Y EN LAS LISTAS acuerdos_simbolos , resoluciones_simbolos Y otros_simbolos SE ENCUENTRAN LOS SIMBOLOS
