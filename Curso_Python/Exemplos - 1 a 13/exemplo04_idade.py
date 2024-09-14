print(50*"-")
print("Bem-vindo, esse programa informa a sua idade ")
print(50*"-")
ano_nascimento = int(input("Informe o ano do seu nascimento: "))
ano_atual = int(input("Informe o ano atual: "))

idade = int(ano_atual-ano_nascimento)

print("Você nasceu no ano de {} e tem {} anos".format(ano_nascimento,idade))
print(50*"-")
