import os

os.system("cls")

print(70*"-")
print("Esse programa mostrará o sucessor e o antecessor do número digitado")
print(70*"-")

numero = float(input("Digite um número: "))

s = numero+1
a = numero-1

print("O número digitado foi {} e o seu sucessor é {} e seu antecessor é {}".format(numero,s,a))

input("Aperte <Enter> para continuar")

os.system("cls")