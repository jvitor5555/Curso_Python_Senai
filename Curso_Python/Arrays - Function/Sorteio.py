import random
import os

os.system("cls")

a1 = str(input("Digite seu nome: "))
a2 = str(input("Digite o segundo nome: "))
a3 = str(input("Digite o terceiro nome: "))

lista = [a1,a2,a3]

escolha = random.choice(lista)

print("O escolhido é o aluno {} ".format(escolha))

