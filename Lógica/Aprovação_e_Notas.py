nota_um = float(input("Digite a primeira nota "))
nota_dois = float(input("Digite a segunda nota "))
nota_final = (nota_um + nota_dois)/2

if(nota_final >= 5):
    print("Você passou:", nota_final)
    if(nota_final >= 8):
        print("Parabéns!")
else:
    print("Você reprovou:", nota_final)
    if(nota_final < 5):
        print("Estude um pouco mais")

