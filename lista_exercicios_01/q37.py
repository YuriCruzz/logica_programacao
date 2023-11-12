# Definição Variavis:
col_segundos = int(input('Incira dados em Segundo: '))

horas = col_segundos // 3600
horas_resto = col_segundos % 3600

minutos = horas_resto // 60
minutos_resto = horas_resto % 60

segundos = minutos_resto // 1
segundos_resto = minutos_resto % 1

# Definição Codigos:
print(horas, 'Horas', minutos, 'Minutos', segundos, 'Segundos')