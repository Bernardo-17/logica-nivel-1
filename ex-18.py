#18) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
numero1 = int(input("Coloque o primeiro numero:"))
numero2 = int(input("Coloque o segundo numero:"))
numero3 = int(input("Coloque o terceiro numero:"))

if(numero1 < numero2):
    if(numero1 < numero3):
        print(numero2 + numero3)
else:
    if(numero2<numero3):
        print(numero3 + numero1)
    else:
        print(numero2 + numero1)

    
