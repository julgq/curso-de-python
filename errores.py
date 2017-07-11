# -*- coding: utf-8 -*-

countries = {
	'mexico': 122,
	'colombia': 49,
	'argentina': 43,
	'chile': 18,
	'peru': 31,
}


while True:
	country = str(raw_input('Escribe el nombre del País: ')).lower()
	try:
		print('La poblaración de {} es: {} millones'.format(country, countries[country]))
	except KeyError:
		print('No tenemos el dato la población de: {} '.format(country))
		

