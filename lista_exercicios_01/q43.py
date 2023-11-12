# Definição Variavis:
notas_1 = int(input('Informe a nota da Materia 01: '))
notas_2 = int(input('Informe a nota da Materia 02: '))
notas_3 = int(input('Informe a nota da Materia 03: '))

frequancia_1 = int(input('Informe a seu numero de falta na Materia 01: '))
frequancia_2 = int(input('Informe a seu numero de falta na Materia 02: '))
frequancia_3 = int(input('Informe a seu numero de falta na Materia 03: '))

# Marerias:
materia_01 = notas_1 >= 7
materia_02 = notas_2 >= 7
materia_03 = notas_3 >= 7

# Frequancia:
frequancia_resu1 = frequancia_1 <= 2
frequancia_resu2 = frequancia_2 <= 2
frequancia_resu3 = frequancia_3 <= 2

# Resuldado:
resultado_1 = (materia_01 and materia_02 and materia_03)
resultado_2 = (frequancia_resu1 and frequancia_resu2 and frequancia_resu3)
resultado_3 = (resultado_1 and resultado_2)

# Definição Codigos:
print('Aluno aprovado?', resultado_3)