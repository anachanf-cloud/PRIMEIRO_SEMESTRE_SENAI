valor_um = float(input("Digite o primeiro valor: "))
valor_dois = float(input("Digite o primeiro valor: "))

escolha = int(input("Calculadora \n Opção 1: Soma \n Opção 2: Subtração \n Opção 3: Multiplicação \n Opção 4: Divisão \n"))

if(escolha == 1):
    resultado_final = valor_um + valor_dois
elif(escolha == 2):
    resultado_final = valor_um - valor_dois
elif(escolha == 3):
    resultado_final = valor_um * valor_dois
elif(escolha == 4):
    resultado_final = valor_um / valor_dois

else:
    print("ERRO")
    resultado_final = 0

print("O resultado é: ", resultado_final)