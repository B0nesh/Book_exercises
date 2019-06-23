#!/usr/bin/python3

text = 'esteperronoesmiperro'

sep = 4

lista = []

texto = ''

iterations = len(text)//4

ciphered = ''

def text_slicer():
	for i in range(iterations):
			if i <= 0:
				lista.append(text[:sep])
			elif i == 1:
				lista.append(text[sep:sep+sep])
			else:
				lista.append(text[sep*i:sep*i+sep])

def substitutioner():
	global ciphered
	for i in range(len(lista)):
		ciphered += f'{lista[i][1]}{lista[i][3]}{lista[i][0]}{lista[i][2]}'
	print(ciphered)
		
text_slicer()
substitutioner()
