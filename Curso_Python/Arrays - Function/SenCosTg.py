print(50*"-")
print("Seja Bem-Vindo, esse programa calcula o Seno, Cosseno e a Tangente ")
print(50*"-")

hipotenusa = float(input("Informe o valor da hipotenusa: "))
ca = float(input("Informe o valor do cateto adjacente: "))
co = float(input("Informe o valor do cateto oposto: "))

print(50*"-")

seno = co/hipotenusa
cosseno = ca/hipotenusa
tangente = co/ca


print(50*"-")

print("O valo de seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(seno,cosseno,tangente))
