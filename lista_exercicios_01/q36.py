# Definição Variavis:
valor = int(input('Informe um valor financeiro: '))

cedulas_100 = valor // 100
resto_100 = valor % 100

cedulas_50 = resto_100 // 50
resto_50 = resto_100 % 50

cedulas_20 = resto_50 // 20
resto_20 = resto_50 % 20

cedulas_10 = resto_20 // 10
resto_10 = resto_20 % 10

cedulas_5 = resto_10 // 5
resto_5 = resto_10 % 5

cedulas_2 = resto_5 // 2
resto_2 = resto_5 % 2

cedulas_1 = resto_2 // 1
resto_1 = resto_2 % 1

# Definição Codigos:
print('Valor a Decompor:', valor)
print(cedulas_100, 'nota(s) de R$ 100,00')
print(cedulas_50, 'nota(s) de R$ 50,00')
print(cedulas_20, 'nota(s) de R$ 20,00')
print(cedulas_10, 'nota(s) de R$ 10,00')
print(cedulas_5, 'nota(s) de R$ 5,00')
print(cedulas_2, 'nota(s) de R$ 2,00')
print(cedulas_1, 'nota(s) de R$ 1,00')