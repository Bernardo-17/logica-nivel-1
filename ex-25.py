#25) Somar números positivos digitados pelo usuário até que ele digite um número negativo
numero = int(input("Digite um número: "))
proximo_numero = int(input("Digite outro número: "))
while numero > 0 and proximo_numero > 0:
     print(numero + proximo_numero)
     numero = int(input("Digite um número: "))
     proximo_numero = int(input("Digite outro número: ")) 
print("Você digitou um número negativo, o programa foi encerrado.")
    
