# Definição Variavis:
recebimento = int(input('Informe sua idade em dias: '))

anos =  recebimento // 365
anos_resto = recebimento % 365

meses = anos_resto // 30
meses_resto = anos_resto % 30

dias = meses_resto // 1
dias_resto = meses_resto % 1

# Definição Codigos:
print(anos, 'Anos', meses, 'Meses', dias, 'Dias')