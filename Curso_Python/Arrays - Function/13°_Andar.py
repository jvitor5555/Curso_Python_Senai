

import os

os.system("cls")

# Números do andar em ordem crescente utilizando FOR 

for numero in range(0,21):
    if numero==13:
        continue
    print(numero)


print(50*("-"))    

# Números do andar em ordem decrescente utilizando FOR    
    
for numero in range(41,0,-1):
    if numero==13:
        continue
    print(numero)
    
# Números do andar em ordem decrescente utilizando WHILE  
teste = 0
andar = 21

while andar>teste:
    andar = andar -1
    if andar == 14:
        continue
    print(andar)
    
    
    
os.system("timeout 06")
os.system("cls")   
    
    