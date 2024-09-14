import os

os.system("cls")

print(50*"-")
print("Bem-Vindo, esse programa converte dollares em reais: ")
print(50*"-")

cotacao = float(input("Informe a cotação atual do dollar: "))
print(50*"-")
dollar = float(input("Informe quantos dollares você possui: "))

print(50*"-")

valor = float(dollar*cotacao)

print("A cotação do dollar hoje é {:.2f} e seus {:.2f} dollares correspondem a {:.2f} reais ".format(cotacao,dollar,valor))

print(50*"-")

