def felizometro(contador):
    if contador <= 1:
        print('\nAah!! Vamos lá, você não está tão desamimado(a) assim para o natal né??')
    else:
        feliz = "Feliz N" + "a" * (contador-1) + "tal!!!!"
        print('\n', feliz)

entrada = int(input('Diaga o ção feliz você está com o natal: '))

felizometro(entrada)