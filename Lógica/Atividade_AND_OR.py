escolha = int(input("Calculadora\n Opção 1: Aprovação e Notas\n Opção 2: Valor dos Carros\n Opção 3: Dados incorretos\n Opção 4: Gols Prós e Contras\n bOpção 5: Salário de Funcionários\n Opção 6: Maiores e Menores \n Opção 7: Maiores que 10\n"))

if(escolha == 1):
    nota_um = float(input("Digite a primeira nota "))
    nota_dois = float(input("Digite a segunda nota "))
    if((nota_um > 5 and nota_dois > 5) or (nota_um > 9 or nota_dois > 9)):
        print("Você passou")

elif(escolha == 2):
    carro_um = float(input("Digite o valor do primeiro carro: "))
    carro_dois = float(input("Digite o valor do segundo carro: "))
    carro_três = float(input("Digite o valor do terceiro carro: "))
    if(carro_um > 20000 and carro_dois > 20000 and carro_três > 20000):
        print("ALERTA\nRICO!")
    elif(carro_um > 50000 or carro_dois > 50000 or carro_três > 50000):
        print("ALERTA\nMUITO RICO")
    else:
        print("Sinto muito, mas talvez você seja pobre.")

elif(escolha == 3):
    número_um = float(input("Digite aqui o primeiro número: "))
    número_dois = float(input("Digete aqui o segundo número: "))
    número_três = float(input("Digete aqui o terceiro número: "))
    número_quatro = float(input("Digete aqui o quarto número: "))
    número_cinco = float(input("Digete aqui o quinto número: "))
    if((número_um + número_dois + número_três + número_quatro + número_cinco < 0) or número_um > 400 or número_dois
       > 400 or número_três > 400 or número_quatro > 400 or número_cinco > 400):
        print("OS DADOS ESTÃO INCORRETOS.")

elif(escolha == 4):
    golscontras = int(input("Digite quantos gols seu time sofreu: "))
    golsprós = int(input("Digite quantos gols seu time fez: "))
    if(golscontras > golsprós):
        print("O SALDO ESTA NEGATIVO.")
    if(golsprós > 18):
        print("SEU ATAQUE ESTÁ MUITO BOM")

elif(escolha == 5):
    valor_um = float(input("Digite o salário do primeiro funcionário: "))
    valor_dois = float(input("Digite o valor do salário do segundo funcionário: "))
    valor_três = float(input("Digite o valor do salário do terceiro funcionário: "))
    média = (valor_um + valor_dois + valor_três) / 3
    if(valor_um < valor_dois and valor_um < valor_três):
        diferença_um = valor_um - média
        print("O menor salário é de " , valor_um , " e a sua diferença da média é de " , diferença_um ,)
    elif(valor_dois < valor_um and valor_dois < valor_três):
        diferença_dois = valor_dois - média
        print("O menor salário é de " , valor_dois , " e a sua diferença da média é de " , diferença_dois ,)
    elif(valor_três < valor_um and valor_três < valor_dois):
        diferença_três = valor_três - média
        print("O menor salário é de " , valor_três , " e a sua diferença da média é de " , diferença_três ,)

elif(escolha == 6):
# O usuario ira digitar 4 numeros, mostre o menor e o maior usando AND nos ifs e não ifs encadeados.
    um = float(input("Digite o primeiro número: "))
    dois = float(input("Digite o segundo número: "))
    três = float(input("Digite o terceiro número: "))
    quatro = float(input("Digite o quarto número: "))

    if(um<dois and um<três and um<quatro):
        print(um , " é o menor.")
    elif(dois<um and dois<três and dois<quatro):
        print(dois , " é o menor.")
    elif(três<dois and três<um and três<quatro):
        print(três , " é o menor.")
    elif(quatro<dois and quatro<três and quatro<um):
        print(quatro , " é o menor.")

    if(um>dois and um>três and um>quatro):
        print(um, " é o maior")
    elif(dois>um and dois>três and dois>quatro):
        print(dois, " é o maior")
    elif(três>dois and três>um and três>quatro):
        print(três, " é o maior")
    elif(quatro>dois and quatro>três and quatro>um):
        print(quatro, " é o maior")

   
elif(escolha == 7):
    number1= float(input("Digite o primeiro número: "))
    number2 = float(input("Digite o segundo número: "))
    number3 = float(input("Digite o terceiro número: "))
    number4 = float(input("Digite o quarto número: "))
    number5 = float(input("Digite o quinto número: "))
    number6 = float(input("Digite o sexta número: "))
    if(number1 > 10):
        print("O número",number1, "é grande.")
    if(number2 > 10):
        print("O número",number2, "é grande.")
    if(number3 > 10):
        print("O número",number3, "é grande.")
    if(number4 > 10):
        print("O número",number4, "é grande.")
    if(number5 > 10):
        print("O número",number5, "é grande.")
    if(number6 > 10):
        print("O número",number6, "é grande.")