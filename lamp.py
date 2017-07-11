# -*- coding: utf-8 -*-

class Lamp:
	_LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
	
	def __init__(self, _is_turned_on):
		self._is_turned_on = _is_turned_on
    	# Definición de una variable privada, _ por cada espacio e inicio.

	def turn_on(self):
		self._is_turned_on = True
		self._display_image()

	def turn_off(self):
		self._is_turned_on = False
		self._display_image()

	# Definición de un metodo privado, lleva _ por cada espacio.
	def _display_image(self):
		if self._is_turned_on:
			print(self._LAMPS[0])
		else:
			print(self._LAMPS[1])

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