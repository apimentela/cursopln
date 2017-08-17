# -*- coding: utf-8 -*-

'''
El ejercicio consiste en que la función de riqueza léxica reciba texto en lugar de una lista de tokens
'''

import nltk

def riqueza_lexica(texto):
	tokens=nltk.word_tokenize(texto,"spanish")
	tokens_conjunto=set(tokens)
	palabras_totales=len(tokens)
	palabras_diferentes=len(tokens_conjunto)
	riqueza_lexica=palabras_diferentes/palabras_totales
	return riqueza_lexica
