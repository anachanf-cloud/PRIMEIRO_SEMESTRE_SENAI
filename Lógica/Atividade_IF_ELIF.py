escolha = int(input("Calculadora \n Opção 1: Números Inteiros \n Opção 2: Maior de idade? \n Opção 3: Comparando Números \n Opção 4: É par ou ímpar?  \n Opção 5: Estou Aprovado? \n Opção 6: Centenas \n Opção 7: Múltiplos de 5? \n Opção 8: Seu Salário \n Opção 9: Qual é o Maior? \n Opção 10: Conceituando as Notas \n Opção 11: Faixa Etária \n Opção 12: Calcule seu IMC \n Opção 13: Entre Números \n Opção 14: Calculando Velocidade \n Opção 15: Descontos \n Opção 16: Cumprimentos Diários \n Opção 17: Processo de Login \n Opção 18: Identificando Triângulos \n Opção 19: Número Primos \n Opção 20: Forma de Pagamento \n Opção 21: Temperaturas \n Opção 22: Números Divisíveis \n"))

if(escolha == 1):
    valor = int(input("Digite o primeiro valor: "))
    if(valor == 0):
        print ("Número Zero")
    elif(valor < 0):
        print ("Número Negativo")
    elif(valor > 0):
        print("Número Positivo")

elif(escolha == 2):
    idade = int(input("Qual sua idade? "))
    if(idade >= 18):
        print("Você é Maior de Idade")
    elif(idade <= 18):
        print("Você é Menor de Idade")

elif(escolha == 3):
    número_um = float(input("Digite aqui o primeiro número: "))
    número_dois = float(input("Digete aqui o segundo número: "))
    if (número_um > número_dois):
        print(número_um ," é maior que ", número_dois)
    else:
        print(número_dois ," é maior que ", número_um)

elif(escolha == 4):
    valor_um = int(input("Digite aqui o número: ")) 
    resto = valor_um % 2
    if(resto == 0):
        print("O Número é PAR")
    else:
        print("O Número é ÍMPAR")

elif (escolha == 5):
    nota = float(input("Digite sua nota "))
    if(nota >= 6):
        print("Você está APROVADO, com a nota ", nota)
        if(nota >= 8):
            print("Parabéns!")
    else:
        print("Você está REPROVADO, com a nota ", nota)
        if(nota < 4):
            print("Estude um pouco mais!")

elif (escolha == 6):
    valor_dois = float(input("Digite aqui o número: 6"))
    if(valor_dois == 100):
        print("Seu valor é IGUAL a 100")
    elif(valor_dois > 100):
        print("Seu número é MAIOR que 100")
    elif(valor_dois < 100):
        print("Seu número é MENOR que 100")

elif (escolha == 7):
    valor_três = int(input("Digite aqui o número: ")) 
    resto_1 = valor_três % 5
    if(resto_1 == 0):
        print("O Número É Múltiplo de 5")
    else:
        print("O Número Não É Múltiplo de 5")

elif (escolha == 8):
    salário = float(input("Digite aqui o seu salário: "))
    if(salário > 2000):
        print("Você GANHA mais que R$2000.00")
    else:
        print("Você NÃO ganha mais que R$2000.00")

elif (escolha == 9): 
    um = int(input("Digite aqui o primeiro valor: ")) 
    dois = int(input("Digite aqui o segundo valor: ")) 
    três = int(input("Digite aqui o terceiro valor: ")) 
    if(um > dois and um > três):
        print(um , " é MAIOR que todos os valores.")
    elif(dois > um and dois > três):
        print(dois , " é MAIOR que todos os valores.")
    elif(três > um and três > dois):
        print(três , " é MAIOR que todos os valores.")

elif (escolha == 10):
    suanota = float(input("Digite sua nota: "))
    if(suanota >= 9):
        print("Sua nota é A")
    elif(suanota >= 7 and suanota < 9):
        print("Sua nota é B")
    elif(suanota >= 5 and suanota < 7):
        print("Sua nota é C")
    elif(suanota < 5):
        print("Sua nota é D")

elif (escolha == 11):
    suaidade = float(input("Digite sua idade: "))
    if(suaidade >= 0 and suaidade <= 12):
        print("Você é uma CRIANÇA")
    elif(suaidade >= 13 and suaidade <= 17):
        print("Você é um ADOLECENTE")
    elif(suaidade >= 18 and suaidade <= 59):
        print("Você é um ADULTO")
    else:
        print("Você é um IDOSO")

elif (escolha == 12):
    seu_peso = float(input("Digite aqui seu peso em KG: "))
    sua_altura = float(input("Digite aqui sua altura em METROS: "))
    seu_IMC = seu_peso / (sua_altura * sua_altura)
    print("Seu IMC é" , seu_IMC)

elif (escolha == 13):
    valor_quatro = float(input("Digite seu número: "))
    if(valor_quatro > 10 and valor_quatro < 50):
        print("Seu número ESTÁ entre 10 & 50")
    else:
        print("Seu número NÃO ESTÁ estre 10 & 50")

elif (escolha == 14):
    velocidade = float(input("Digite a velocidade em KM/h: "))
    if(velocidade < 80):
        print("Você está dentro do limetes.")
    elif(velocidade > 80 ):
        MULTA = (velocidade - 80) * 5 
        print("Você terá que pagar", MULTA , "reais")

elif (escolha == 15):
    compra = float(input("Digite aqui o valor da compra: "))
    if(compra > 500):
        APAGAR = compra - (compra/ 100 * 10)
        print("Você pagará o total de" , APAGAR , "reais")
    elif(compra > 300 and compra < 500):
        APAGAR1 = compra - (compra/ 100 * 5)
        print("Você pagará o total de" , APAGAR1 , "reais")
    else:
        print("Você não terá desconto")

elif (escolha == 16):
    horário = float(input("Qual horário?: "))
    if(horário >= 5 and horário < 12):
        print("Bom dia!")
    elif(horário >= 12 and horário < 18):
        print("Boa tarde")
    elif(horário >= 18 and horário <24):
        print("Boa noite")
    else:
        print("É MADRUGADA! VÁ DORMIR!")

elif (escolha == 17):
    login = input("Usuário: ")
    senha = int(input("Senha: "))
    if (login == "admin" and senha == 1234):
        print("ACESSO PERMITIDO")
    else:
        print("ACESSO NEGADO")

elif (escolha == 18):
    ladoA = int(input("Valor do lado A: "))
    ladoB = int(input("Valor do lado B: "))
    ladoC = int(input("Valor do lado C: "))
    if (ladoA == ladoB and ladoB == ladoC and ladoC == ladoA):
        print("É um triângulo EQUILÁTERO")
    elif (ladoA == ladoB and ladoB != ladoC and ladoC != ladoA):
        print("É um triângulo ISÓSCELES")
    else:
        print("É um triângulo ESCALENO")

elif (escolha == 19):
    primo = int(input("Digite o número aqui: "))
    CONFIRMAÇÃO = 0 # começa como zero insinuando que se for zero é par (0 ou 1)
    primeiro_primo = 2

    while(primeiro_primo < primo):
        if(primo % primeiro_primo == 0): #divisão exata, encontra o resultado
            CONFIRMAÇÃO = 1 # ele é divisível por outros números
            print(primeiro_primo)
        primeiro_primo = primeiro_primo + 1

        print(primeiro_primo)

    if(CONFIRMAÇÃO == 1):
        #significa que a divisão deu número exato consequentemente: 
        print("NÃO É um número primo!")
    else: 
        #momento algum o reseultado da divisão deu zero, o que significa:
        print ("É um número Primo")


elif (escolha == 20):
    custo = float(input("Valor do produto: "))
    pagamento = int(input("Forma de pagamento: \n 1- Dinheiro \n 2- Cartão \n 3- Parcelamento \n"))
    if(pagamento == 1):
        desconto = custo - (custo/ 100 * 10)
        print("Você pagará o total de" , desconto , "reais, se pagar no dinheiro.")
    elif(pagamento == 2):
        desconto_1 = custo - (custo/100*5)
        print("Você pagará o total de" , desconto_1 , "reais, se pagar no cartão.")
    elif(pagamento == 3):
        desconto_2 = custo + (custo/100*10)
        print("Você pagará o total de" , desconto_2 , "reais, se pagar parcelado.")
    
elif (escolha == 21):
    temperatura = float(input("Digite aqui a temperatura: "))
    if(temperatura <= 15):
        print("O clima está FRIO!")
    elif(temperatura >= 15 and temperatura < 25):
        print("O clima está AGRADÁVEL!")
    elif(temperatura >= 25):
        print("O clima está QUENTE!")

elif (escolha == 22):
    op_um = float(input("Digite aqui o primeiro número: "))
    op_dois = float(input("Digite aqui o segundo número: "))
    resultado = op_um % op_dois
    if (resultado == 0):
        print("Os números ", op_um , "e" , op_dois , " são DIVISÍVEIS.")
    else:
        print("Os números ", op_um , "e" , op_dois , " NÃO são DIVISÍVEIS.")