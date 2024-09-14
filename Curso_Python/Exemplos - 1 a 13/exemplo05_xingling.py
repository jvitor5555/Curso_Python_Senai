import os

os.system("cls")

print(50*"-")

compra = float(input("Informe o valor da sua compra: "))

parcelas = int(input("Informe o valor das parcelas: "))

valor_parcela = compra/parcelas

print(50*"-")

if (parcelas>5):
    porcento = parcelas/100
    juros = porcento*compra
    valor_juros = juros+compra
    print("Sua compra de {:.2f} reais recebeu um juros de {:.2f} reais e terá o valor de {:.2f} reais ".format(compra,juros,valor_juros))
    print(50*"-")
else:
    print("O valor da sua compra foi de {:.2f} e será pago em {:.2f} parcelas de {:.2f} reais".format(compra,parcelas,valor_parcela))
    print(50*"-")

    