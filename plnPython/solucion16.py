# -*- coding: utf-8 -*-

'''
El ejercicio consiste en que la función de riqueza léxica reciba texto en lugar de una lista de tokens
'''

import nltk

def porcentaje(palabra,texto):
	tokens=nltk.word_tokenize(texto,"spanish")
	conteo_individual=tokens.count(palabra)
	palabras_totales=len(tokens)
	tokens_conjunto=set(tokens)
	palabras_diferentes=len(tokens_conjunto)
	porcentaje=100*conteo_individual/palabras_totales
	return porcentaje
