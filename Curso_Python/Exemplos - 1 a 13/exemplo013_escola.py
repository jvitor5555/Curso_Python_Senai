import os
os.system("cls")

print(50*"-")
print("Esse programa calcula o sálario do professor")
print(50*"-")

nivel = int(input("Informe o seu nível, por favor: "))
aulas = float(input("Informe a quantidade de aulas: "))

if nivel==1:
    salario = aulas*12
    print("A quantidade de aulas foi de {:.2f} e corresponde a um sálario de {:.2f}".format(aulas,salario))
elif nivel==2:
    salario = aulas*17
    print("A quantidade de aulas foi de {:.2f} e corresponde a um sálario de {:.2f}".format(aulas,salario))
elif nivel==3:
    salario = aulas*25
    print("A quantidade de aulas foi de {:.2f} e corresponde a um sálario de {:.2f}".format(aulas,salario))
else:
    print("<Opção Inválida> --- Reinicie o programa para tentar novamente")
