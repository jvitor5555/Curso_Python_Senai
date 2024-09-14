import os
os.system("cls")

print(50*"-")
print("Seja bem-vindo, esse programa calcula o preço das compras e seu repectivo desconto")
print(50*"-")

nome_produto = str(input("Informe o nome do produto: "))

quantidade_produto = int(input("Informe a quantidade do produto: "))

preco_produto = float(input("Informe o preço do produto: "))

print(50*"-")

total_produto = quantidade_produto*preco_produto

if quantidade_produto<=5:
    desconto = total_produto*0.02
    valor_final = total_produto - desconto
    print("O valor da sua compra é de {:.2f} e com o desconto ficará {:.2f}".format(total_produto,valor_final))
elif quantidade_produto>5 and quantidade_produto<=10:
    desconto = total_produto*0.03
    valor_final = total_produto - desconto
    print("O valor da sua compra é de {:.2f} e com o desconto ficará {:.2f}".format(total_produto,valor_final))
else:
    desconto = total_produto*0.05
    valor_final = total_produto - desconto
    print("O valor da sua compra é de {:.2f} e com o desconto ficará {:.2f}".format(total_produto,valor_final))
