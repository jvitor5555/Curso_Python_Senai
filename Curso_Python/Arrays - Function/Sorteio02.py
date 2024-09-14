import random

a1 = str(input("Digite um nome: "))
a2 = str(input("Digite o segundo nome: "))
a3 = str(input("Digite o terceiro nome: "))

lista = [a1,a2,a3]

escolha = random.shuffle(lista)

print("A ordem de apresentação é: ")
print(lista)