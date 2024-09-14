import os

os.system("cls")

print(50*"-")
print("Esse programa informa se um número é par ou impar")
print(50*"-")

n1 = float(input("Informe um número: "))

resto  = n1%2

if resto==0:
    print("O número {:.2f} é par".format(n1))
else:
    print("O número {:.2f} é impar".format(n1))