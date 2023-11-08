# Definição Variavis:
a = int(input('Defina a Variavrel "Dias"; '))
b = int(input('Defina a Variavrel "Horas"; '))
c = int(input('Defina a Variavrel "Minutos"; '))
d = int(input('Defina a Variavrel "Segundos"; '))

d_s = (a*86400)
h_s = (b*3600)
m_s = (c*60)

# Definição Codigos:
print('Segundos Totais;',d_s+h_s+m_s+d)