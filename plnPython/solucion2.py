# -*- coding: utf-8 -*-

'''
A partir de este ejercicio cambiamos las rutas absolutas por relativas y se utiliza la codificación UTF-8
'''

carpeta_nombre="Documentos\\"
archivo_nombre="P_IFT_200416_162_Acc.txt"

palabra1="ACUERDO"
palabra2="RESOLUCIÓN"

with open(carpeta_nombre+archivo_nombre,"r",encoding="utf8") as archivo:
	texto=archivo.read()
	
if palabra1 in texto:
	print("El documento es un(a)",palabra1)
	
elif palabra2 in texto:
	print("El documento es un(a)",palabra2)
	
else:
	print("El documento no es ni un ACUERDO ni una RESOLUCIÓN")
