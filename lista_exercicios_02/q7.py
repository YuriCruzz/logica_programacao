# Definição Variavis:
a = float(input('Informe a Variavel A: '))
b = float(input('Informe a Variavel B: '))
c = float(input('Informe a Variavel C: '))
d = float(input('Informe a Variavel D: '))

# Definição Codigos:

if (b > c) and (d > a) and (c + d > a + b) and (c > 0) and (d > 0) and (a % 2 == 0):
    print('Valores Aceitos!')
else:
    print('Valores não Aceitos')