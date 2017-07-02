# -*- coding: utf-8 -*-

"""
"abacabad" c y d no se repiten
"abacabaabacaba" _ todos se repiten
"bccccccccccyb" y no se repite
"""

def first_no_repeating_char(char_sequence):
	seen_letters = {}

	for idx, letter in enumerate(char_sequence):
		print('Imprimo idx: {} letter: {}'.format(idx, letter))
		print("------")
		if letter not in seen_letters:
			seen_letters[letter] = (idx, 1)

		else:
			print(seen_letters[letter][0])
			print(seen_letters[letter][1]+1)
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1]+1)

		print('seen_letters: ')
		print(seen_letters)
		print("")

	final_letters = []
	for key, value in seen_letters.iteritems():
		if value[1] == 1:
			final_letters.append((key, value[0]))

	not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

	if not_repeated_letters:
		return not_repeated_letters[0][0]
	else:
		return '_'


if __name__ == '__main__':
	char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))
	print(char_sequence)
	print('-')

	result = first_no_repeating_char(char_sequence)

	if result == '_':
		print('Todos los caracteres se repiten.')
	else:
		print('El primer caracterer no repido es: {}'.format(result))