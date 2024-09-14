import os

os.system("cls")

print(50*"-")

print("Seja bem-vindo, esse programa informa o maior, menor e igualdade dos números")

print(50*"-")

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segudo número: "))

print(50*"-")

if n1==n2:
    print("Os números são iguais")
    print(n1,"é = a",n2)
elif n1>n2:
    print("O maior número é o {:.2f} e o menor é {:.2f}".format(n1,n2))
else:
    print("O maior número é {:.2f} e o menor é {:.2f}".format(n2,n1))