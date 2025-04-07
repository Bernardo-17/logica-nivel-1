#Classificação de Idade - Peça ao usuário sua idade e classifique da seguinte forma:
#Menor de 12 anos: Criança
#Entre 12 e 17 anos: Adolescente
#Entre 18 e 59 anos: Adulto
#60 anos ou mais: Idoso
idade = int(input("Qual a sua idade?"))
if(idade < 12):
    print("Voce é Criança")
elif(idade >= 12) and (idade <= 17):
    print("Voce e adolescente")
elif(idade >= 18) and (idade <= 59):
    print("Voce é adulto")
elif(idade >= 60):
    print("Voce é idoso")
else:
    print("Idade inválida")
