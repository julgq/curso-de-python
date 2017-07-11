# -*- coding: utf-8 -*-

def run():
	counter = 0
	with open('lectura.txt') as f:
		print(f.readlines())
		for line in f:
			counter += line.count('Julio')

	print('Beatriz se encuentra {} en el texto'.format(counter))

if __name__ == '__main__':
	run()