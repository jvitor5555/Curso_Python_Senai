print(50*"-")
print("Bem-vindo ao programa que gera a sequência da equipe :) ")
print(50*"-")

nome = str(input("Digite o nome da sua equipe: "))

numero = int(input("Digite o número de participantes da equipe:"))

cont = 0

while cont < numero:
    cont = cont + 1
    print("Equipe {} {}".format(nome,cont))
