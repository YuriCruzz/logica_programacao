# Definição Variavis:
salario = float(input('Informe seu salario: '))

parametro = 1250

# Definição Codigos:

if salario > parametro:
    calculo = salario * 0.10
    salario = salario + calculo
    print(f'Seu almento é de {calculo}')
    print(f'Assim, você deve receber {salario}')
elif salario <= parametro:
    calculo = salario * 0.15
    salario = salario + calculo
    print(f'Seu almento é de {calculo}')
    print(f'Assim, você deve receber {salario}')