#Verificação de Nota - Peça ao usuário para digitar sua nota (0 a 10) e classifique:
#Nota ≥ 7: Aprovado
#Nota entre 5 e 6.9: Recuperação
#Nota < 5: Reprovado

Nota  = float(input("Qual a nota da sua prova?"))
if(Nota >= 7):
    print("Aprovado")
elif(Nota >= 5) and (Nota <= 6.9):
    print("Recuperação")
elif(Nota < 5):
    print("Reprovado")
