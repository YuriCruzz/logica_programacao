# Questão A e C:
def quadrado (tamanho, exibir=False):
    if exibir == True:
        return tamanho**2
    else:
        print('Torne a Variavel Valida!')

lado = int(input('Informe o tamanho do lado do Quadrado: '))
t_f = input('Precione "V" para Verdadeiro e "F" para Falso: ')

if t_f == 'F' or t_f == 'f':
    t_f = False
elif t_f == 'V' or t_f == 'v':
    t_f = True

print(quadrado(lado, t_f))

# Questão B e C:
def triangulo (p1, p2, exibir=False):
    if exibir == True:
        soma = int((p1 * p2)/2)
        return soma
    else:
        print('Torne a Variavel Valida!')

# Entradas.
base = int(input('Informe a tamanho da base do Triângulo: '))
altura = int(input('Informe a tamanho da altura do Triângulo: '))
t_f2 = input('Precione "V" para Verdadeiro e "F" para Falso: ')

# Verifição de variaval "t_f2" e comvercor.
if t_f2 == 'F' or t_f2 == 'f':
    t_f2 = False
elif t_f2 == 'V' or t_f2 == 'v':
    t_f2 = True

print(triangulo(base, altura, t_f2))