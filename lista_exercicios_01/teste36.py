# Deixei apenas para você poder ver como estava. É uma replica do codico, por que eu tentei refazer para poder entender mais ou menos como fazia.



# Definição Variavis:
def calcular(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    qtn_notas = [0, 0, 0, 0, 0, 0, 0]

    print('Valor: ', valor)

    for i in range(len(notas)):
        qtn_notas[i] = valor // notas[i]
        valor %= notas[i]

    for i in range(len(notas)):
            if qtn_notas[i] > 0:
                print(f'{qtn_notas[i]} nota(s) de {notas[i]}')

# Definição Codigos:
valor = int(input('Defina a Variavrel "Cédulas"; '))
calcular(valor)