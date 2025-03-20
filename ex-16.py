#16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
numero = int(input(" Digite o numero de maçâs que deseja?"))
if(numero<12):
    print ("Da um total de",numero * 1.3,"reais.")
else:
    print ("Da um total de",numero * 1,"reais")
