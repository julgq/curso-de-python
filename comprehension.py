# -*- coding: utf-8 -*-

# SUGAR SYNTAX
# List comprehension
# Escribr una lista de numeros pares:

pares = []

# Metodo Tradicional:

pares = []
for num in range(1,31):
	if num % 2 == 0:
		pares.append(num)

print (pares)

# Metodo List Comprehension

even = [num for num in range(1, 31) if num % 2 == 0]
print(even)


# Dictionary comprehension

# Metodo Tradicional:
cuadrados = {}

for num in range(1, 11):
	cuadrados[num]= num**2

print(cuadrados)

# Metodo Dictionary comprehension:

squares = {num: num**2 for num in range(1, 11)}
print(squares)



