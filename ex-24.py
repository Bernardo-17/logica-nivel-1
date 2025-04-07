#24) Pedir senha até que seja digitada a correta
senha = "116"
senhadigitada = input("Digite a senha:")
while senha != senhadigitada:
    print("Senha incorreta")
    senhadigitada = input("Digite a senha:")
print("seja bem-vindo")
