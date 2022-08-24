
numeroRomano = input('Informe o numero romano: \n').upper()
numeroRomanoList = list(numeroRomano) # Transformando String em List para poder validar ordem dos algarismos

validadeRomano = True # Booleano para validação do número romano

# Substituindo algarismos romanos por seus equivalentes numerais
for i, num in enumerate(numeroRomanoList):
    if num == 'I':
        numeroRomanoList[i] = 1
    elif num == 'V':
        numeroRomanoList[i] = 5
    elif num == 'X':
        numeroRomanoList[i] = 10
    elif num == 'L':
        numeroRomanoList[i] = 50
    elif num == 'C':
        numeroRomanoList[i] = 100
    elif num == 'D':
        numeroRomanoList[i] = 500
    elif num == 'M':
        numeroRomanoList[i] = 1000
    else: # Bloco else para invalidar outros algarismos
        validadeRomano = False
        print('Esse número romano é inválido pela invalidade dos algarismos informados. Tente novamente!')
        exit()


# Invalidando por quantidade máxima de algarismos repetidos - V, L e D não podem se repetir
if numeroRomanoList.count(5) > 1 or numeroRomanoList.count(50) > 1 or numeroRomanoList.count(500) > 1:
    validadeRomano = False
    print('Esse número romano é inválido pela quantidade de algarismos repetidos. Tente novamente!')
    exit()

# I, X, C, M não podem se repetir mais de 3 vezes consecutivas
if len(numeroRomanoList) > 3:
    for i, num in enumerate(numeroRomanoList):
        if i+3 == len(numeroRomanoList): # Parando verificação para não ocorrer erro de indice fora do range
            break
        if num == numeroRomanoList[i + 1] and num == numeroRomanoList[i + 2] and num == numeroRomanoList[i + 3]:
            validadeRomano = False
            print('Esse número romano é inválido pela quantidade de algarismos repetidos. Tente novamente!')
            exit()


subtracao = 0 # Variavel para guardar valores a serem subtraidos do resultado final

# Validando ordem dos algarismos e lógica da subtração
for i, num in enumerate(numeroRomanoList):
    if i+1 == len(numeroRomanoList):
        break
    elif num < numeroRomanoList[i+1]:
        # I, X e C podem ser escritas atrás de outros algarismos para subtrair - I só antes do V e X | X só antes do L e C | C só antes do D e M
        if (num == 1 and (numeroRomanoList[i+1] == 5 or numeroRomanoList[i+1] == 10)) or (num == 10 and (numeroRomanoList[i+1] == 50 or numeroRomanoList[i+1] == 100)
        ) or (num == 100 and (numeroRomanoList[i+1] == 500 or numeroRomanoList[i+1] == 1000)):
            subtracao += num
        else:
            validadeRomano = False
            print('Esse número romano é inválido pela ordem informada dos algarismos. Tente novamente!')
            exit()


# Calculando e mostrando resultado
if validadeRomano == True:
    print('O número romano informado é válido!')
    numeroRomanoConvertido = 0

    for num in numeroRomanoList:
        numeroRomanoConvertido += num

    numeroRomanoConvertido -= subtracao*2

    print(f'Numero romano convertido: {numeroRomanoConvertido}')



