#13 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
anos = int(input("Qual a sua idade em anos?"))
meses = int(input("qual o mês em que nasceu?"))
print (anos * 365 + meses * 30)
