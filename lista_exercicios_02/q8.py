# Definição Variavis:
h_inicial = int(input('Insira a Hora inicial: '))
m_inicial = int(input('Insira o Minuto inicial: '))
h_final = int(input('Insira a Hora final: '))
m_final = int(input('Insira o Minuto final: '))

# Definição Codigos:
inicio_minutos = h_inicial * 60 + m_inicial
fim_minutos = h_final * 60 + m_final
d_minutos = fim_minutos - inicio_minutos

if d_minutos <= 0:
    d_minutos += 24 * 60  # Adicionar 24 horas

duracao_horas = d_minutos // 60
duracao_minutos = d_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")