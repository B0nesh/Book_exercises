#!/usr/bin/python3

text = 'esteperronoesmiperro'

table = 'abcdefghijklmnopqrstuvwxyz'

size = 4 

iterations = len(text)//size

chunks = []

ciphered = ''


def text_slice():
	for i in range(iterations):
		if i <= 0:
			chunks.append(text[:size])
		elif i == 1:
			chunks.append(text[size:size+size])
		else:
			chunks.append(text[size*i:size*i+size])

def conversion():
	global ciphered
	for i in range(len(chunks)):
		for u in range(len(chunks[i])):
			if u == 0:
				ciphered += f'{table[table.find(chunks[i][u])+2]}'
			elif u == 1:
				ciphered += f'{table[table.find(chunks[i][u])+5]}'
			elif u == 2:
				ciphered += f'{table[table.find(chunks[i][u])+3]}'
			else:
				ciphered += f'{table[table.find(chunks[i][u])+1]}'
	print(ciphered)

text_slice()
conversion()