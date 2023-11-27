# Definição Variavis:
p_mes = int(input('Escolha um número de 1 a 12: '))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
if p_mes > 12:
    print('Número celecionado não compativel! Por favor escoloha um numero valido!')
else:
    print(meses[p_mes - 1])