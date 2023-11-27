# Definição Variavis:
preco = float(input('Informe a distancia (em km) que deseja percorrer: '))


# Definição Codigos:

if preco <= 200:
    n = preco * 0.50
    print(f'Você deve pagar {n} para fazer a viagem.')
else:
    n = preco * 0.45
    print(f'Você deve pagar {n} para fazer a viagem.')