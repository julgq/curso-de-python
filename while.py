# -*- coding: utf-8 -*-
import random

def run():
	number_found = False
	randamon_number = random.randint(0,20)

	while not number_found:
		number = int(raw_input('Intenta un número: '))

		if number == randamon_number:
			print('Felicidades. Encontraste el número')
			number_found = True
		elif number > randamon_number:
			print('El número es mas pequeño')
		else:
			print('El número es más grande')


if __name__ == '__main__':
	run()