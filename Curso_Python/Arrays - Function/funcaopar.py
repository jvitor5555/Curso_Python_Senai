def Calcular_Par():
    
    while True:
    
        try:
            
            v1 = int(input("Informe um número Par: "))
            
            par = v1 % 2
            
            
            
            if par == 0:
                resultado = "O número digitado é PAR"
                print(resultado)
                
            else:
                resultado = "Informe Somente Números Pares"
                print(resultado)
                
            
            
        except:
            print("Caracter Inválido, Forneça Apenas um Número Par")