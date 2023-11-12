# Definição Variavis:

# R. A: Primeiro foi executado a exponenciação, em seguida o "menor que" e o "igual a" (==), em ordem de aparição, da esquerda para a direita. Por fim a conjunção (end).
a = 3 < 2 ** 3 and 3 == 3

# R. B: Primeiro foi executado o que está dentro dos parênteses, na ordem; parêntesees de dentro com soma, divisão, em ordem, da esquerda para a direita, em seguida o "igual a", a conjunção (end), e por fim o que estava fora do parênteses, primeiro o "diferente de" e a disjunção (or) para finalizar.
b = 0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2)

# Definição Codigos:
print('Resposta A:', a)
print('Resposta B:', b)