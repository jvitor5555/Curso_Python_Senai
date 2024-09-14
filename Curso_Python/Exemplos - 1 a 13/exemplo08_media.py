import os

os.system("cls")

print(50*"-")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

print(50*"-")

if (media>=5):
    print("<Aprovado> - - - sua nota é {:.2f} - - -".format(media))
    print(50*"-")
    
else:
    print("<Reprovado> - - - sua nota é {:.2f} - - - ".format(media))
    print(50*"-")

    