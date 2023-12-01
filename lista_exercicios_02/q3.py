# Definição Variavis:
print('''Informe o tipo de usuario pela sigla;
Residencial (R)
Comercial (C)
Industrial (I)''')
tipo = (input('Sua resposta: '))
energia = int(input('Informe a quantidade de energia gasta (kWh): '))

# Definição Codigos:
match tipo:
    case 'R':
        if energia <= 500:
             resi = energia * 0.40
             print(f'Você deve pagar {resi} de energia!')
        elif energia > 500:
            resi = energia * 0.65
            print(f'Você deve pagar {resi} de energia!')
    case 'C':
        if energia <= 1000:
            come = energia * 0.55
            print(f'Você deve pagar {come} de energia!')
        elif energia > 1000:
            come = energia * 0.60
            print(f'Você deve Pagar {come} de energia!')
    case 'I':
        if energia <= 5000:
            indu = energia * 0.55
            print(f'Você deve pagar {indu} de energia!')
        elif energia > 5000:
            indu = energia * 0.60
            print(f'Você deve Pagar {indu} de energia!')