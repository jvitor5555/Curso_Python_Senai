def Calcular_Ano():
    
    while True:
    
        try:
            
            nome = str(input("Informe o seu Nome Completo, Por Favor: "))
            nome.lower()
            
            while nome.strip() == "":
                raise Exception (print("Informe Seu Nome, Somente Espaços Em Branco Não São Válidos"))
            
            
            ano_nascimento = int(input("Informe o ano do seu Nascimento, Por Favor: "))
            
            if ano_nascimento < 0 or ano_nascimento < 1922 :
                
                raise Exception (print("Formato Incorreto"))
            
            elif ano_nascimento > 2021:
                
                raise Exception (print("Formato Incorreto"))
            
            ano_atual = 2022
            
            resultado = ano_atual - ano_nascimento
            
            print(70*"-")
            print("Seja Bem-Vindo {}, no ano de {} - Você completou ou completará {} anos".format(nome,ano_atual,resultado))
            print(70*"-")
            
        except:
           print("Caro Usuário, Informe Seu <Nome> Apenas Com <Caracteres> e Sua <Idade> Apenas Com <Números>")
       