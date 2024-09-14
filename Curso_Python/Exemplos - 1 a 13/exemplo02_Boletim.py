
print("Seja bem-vido ao Boletim Eletrônico")

# 1 Passo - Entrada de Dados

nome = str(input("Digite seu nome: "))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

# 2 Passo - Processamento dos Dados

media = (n1+n2+n3+n4)/4

# 3 Passo - Saída dos Dados

print("A nota do aluno {} é {:.2f} ".format(nome,media))
