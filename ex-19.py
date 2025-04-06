#19) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.
numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite outro numero:"))
numero3 = int(input("Digite mais um numero:"))

if numero1 > numero2 and numero2 > numero3:
    print("numero1,nemero2,numero3")
elif numero1 > numero3 and numero3 > numero2:
    print("numero1,numero3,numero2")
elif numero2 > numero1 and numero1 > numero3:
    print("numero2,numero1,numero3")
elif numero2 > numero3 and numero3 > numero1:
    print("numero2,numero3,numero1")        
elif numero3 > numero1 and numero1 > numero2:
    print("numero3,numero1,numero2")
elif numero3 > numero2 and numero2 > numero1:
    print("numero3,numero2,numero1")
else:
    print("Existe numeros iguais")    
