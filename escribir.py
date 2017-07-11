# -*- coding: utf-8 -*-
def run():
	
	# Usando manejador de contexto with:

	with open('numeros.txt', 'w') as f: #Manejador de contexto with
		for i in range(0,10):
			f.write(str(i))
		f.close()

	# Usando una forma tradicional

	try:
		f = open('numeros.txt', 'w')
		for i in range(10):
			f.write(str(i))
	finally:
		f.close()

if __name__ == '__main__':
	run()