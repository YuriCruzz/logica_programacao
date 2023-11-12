# Definição Variavis:
valor = float(input('Informe um valor financeiro com centavos: '))

# Cedulas:

cedulas_100 = (valor // 100)
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

# Moedas:

moedas_1 = resto_2 // 1
resto_1 = resto_2 % 1

moedas_050 = resto_1 // 0.50
resto_050 = resto_1 % 0.50

moedas_025 = resto_050 // 0.25
resto_025 = resto_050 % 0.25

moedas_010 = resto_025 // 0.10
resto_010 = resto_025 % 0.10

moedas_005 = resto_010 // 0.05
resto_005 = resto_010 % 0.05

moedas_001 = resto_005 // 0.01
resto_001 = resto_005 % 0.01

# Definição Codigos:
print('NOTAS:')
print(int(cedulas_100), 'nota(s) de R$ 100,00')
print(int(cedulas_50), 'nota(s) de R$ 50,00')
print(int(cedulas_20), 'nota(s) de R$ 20,00')
print(int(cedulas_10), 'nota(s) de R$ 10,00')
print(int(cedulas_5), 'nota(s) de R$ 5,00')
print(int(cedulas_2), 'nota(s) de R$ 2,00')

print('MOEDAS:')
print(int(moedas_1), 'moedas(s) de R$ 1,00')
print(int(moedas_050), 'moedas(s) de R$ 0,50')
print(int(moedas_025), 'moedas(s) de R$ 0.25')
print(int(moedas_010), 'moedas(s) de R$ 0,10')
print(int(moedas_005), 'moedas(s) de R$ 0,05')
print(int(moedas_001), 'moedas(s) de R$ 0,01')