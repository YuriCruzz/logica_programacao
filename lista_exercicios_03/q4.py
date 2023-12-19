def decomposicao(valor):
    # Verificadores.
    notas =  [100, 50, 20, 10, 5, 2, 1]
    qtn_notas = [0, 0, 0, 0, 0, 0, 0]

    print(f'Valor: {valor}')

    # Atulisa "qtn_notas" de acordo com a decomposição.
    for i in range(len(notas)):
        qtn_notas[i] = valor // notas[i]
        valor %= notas[i]

    # Exibe o processo anterior para o Usuario.
    for i in range(len(notas)):
        if qtn_notas[i] >= 0:
            print(f'{qtn_notas[i]} nota(s) de {notas[i]}')

entrada = int(input('Informe um numero para a decomposição: '))

decomposicao(entrada)