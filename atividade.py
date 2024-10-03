import os 
os.system("cls || clear ")
from dataclasses import dataclass

quantidade_de_familiares = 1
lista_familiares = []
lista_salario = []
contator = 0
media = 0
soma_salario = 0
soma_flihos = 0



while True:
    
        print("""
            /t === MENU ===
            1 - adiocionar família
            2 - Exibir resultados
            3 - Sair
        
        """)

        resposta = int(input("deseja adicionar mais uma familia? "))

        match resposta:
            case 1:
                    quantidade_filhos = int(input("digite a sua quantidade de filhos: "))
                    salario = float(input("digite seu salario: "))
                    
                    contator += 1
                    lista_familiares.append(quantidade_filhos)
                    lista_salario.append(salario)
                
            case 2:
                print(f"familias que responderam: {contator}")
                maiorsalario =max(lista_salario)
                menorsalario =min(lista_salario)
                soma_salario =sum(lista_salario)
                media_salario = soma_salario / contator
                soma_flihos =sum(lista_familiares)
                media_filhos = soma_flihos / contator
                print(f"maior salario: {maiorsalario}")
                print(f"menor salario: {menorsalario}")
                print(f"quantidade de filhos: {quantidade_filhos}")
                print(f"media  salarial:  {media_salario}")
                print(f"media de filhos:  {media_filhos}")
                
                
                break
            case 3:
                print("===programa finalizado===")
                break    
            case _:
                print("opção invalida")

#nome_arquivo = "arquivo_familia.txt"

#with open(nome_arquivo, "w") as arquivo_familia:
    #for i in range(1):
        #arquivo_familia.write(f""" familias que responderam: {contator}
            #media  salarial:  {media_salario}
            #media de filhos:  {media_filhos}
            #maior salario: {maiorsalario}, 
            #menor salario: {menorsalario}\n  """)
#arquivo_familia.close()