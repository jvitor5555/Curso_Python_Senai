import os
os.system("cls")

print(70*"-")
print("Seja bem-vindo, esse programa calcula as operações matemáticas")
print(70*"-")
print("Informe um número de acordo com a opção desejada")
print(70*"-")


n1 = float(input("1-Soma, 2-Subtração, 3-Divisão, 4-Multiplicação, 5-Potenciação e 6-Raiz Quadrada \n"))
print(70*"-")
print("Insira os número para a operação")
print(70*"-")

n2 = float(input("Informe o primeiro valor: "))
n3 = float(input("Informe o segundo valor: "))

if n1==1:
    a = n2+n3

    print("O número {:.2f} mais {:.2f} é = {:.2f}".format(n2,n3,a))
elif n1==2:
    a = n2-n3
    print("O número {:.2f} menos {:.2f} é = {:.2f}".format(n2,n3,a))
elif n1==3:
    a = n2/n3
    print("O numero {:.2f} dividido por {:.2f} é = {:.2f}".format(n2,n3,a))
elif n1==4:
    a = n2*n3
    print("O número {:.2f} vezes {:.2f} é = {:.2f}".format(n2,n3,a))
elif n1==5:
    a = n2**n3
    print("O número {:.2f} elevado a {:.2f} é = {:.2f} ".format(n2,n3,a))
elif n1==6:
    a = n2**(1/2)
    b = n3**(1/2)
    print("A raiz quadrada de {:.2f} é {:.2f}".format(n2,a))
    print("A raiz quadrada de {:.2f} é {:.2f}".format(n3,b))
else:
    print("<Opção Inválida> ---- Reinicie o programa para tentar novamente!!!")
