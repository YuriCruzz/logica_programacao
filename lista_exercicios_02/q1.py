# Definição Variavis:
a = int(input('Informe um Número: '))
b = int(input('Informe um Número: '))
c = int(input('Informe um Número: '))


# Definição Codigos:

if a > b and a > c:
    print(f'O maior número é: {a}')
elif b > a and b > c:
    print(f'O maior número é: {b}')
elif c > a and c > b:
    print(f'O maior número é: {c}')

if a < b and a < c:
    print(f'O menor número é: {a}')
elif b < a and b < c:
    print(f'O menor número é: {b}')
elif c < a and c < b:
    print(f'O menor número é: {c}')