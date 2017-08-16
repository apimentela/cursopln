# -*- coding: utf-8 -*-

'''
El ejercicio consiste en hacer un clasificador simple que indica si un documento es un ACUERDO, una RESOLUCIÓN u otro tipo de documento.
'''

carpeta_nombre="C:\\Users\\user\\Desktop\\Documentos\\"
archivo_nombre="P_IFT_200416_162_Acc.txt"

palabra1="ACUERDO"
palabra2="RESOLUCIÓN"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
	texto=archivo.read()
	
if palabra1 in texto:
	print("El documento es un(a)",palabra1)
	
elif palabra2 in texto:
	print("El documento es un(a)",palabra2)
	
else:
	print("El documento no es ni un ACUERDO ni una RESOLUCIÓN")
