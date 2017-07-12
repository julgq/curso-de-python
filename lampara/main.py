# -*- coding: utf-8 -*-

# Del modulo lamp, importa la Clase Lamp
from lamp import Lamp

def run():
	lamp = Lamp(_is_turned_on=True)

	while True:
		command = str(raw_input('''
			¿Qué deseas hacer?
			[p]render
			[a]pagar
			[s]alir
			'''))

		if command == 'p':
			lamp.turn_on()
		elif command == 'a':
			lamp.turn_off()
		else:
			break

if __name__ == '__main__':
	run()