print("""
    Integrantes:
    Amanda Almeida Lima dos Santos
    Miguel Lemos de Oliveira Esquivel
""")

import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Dados:
    salario: float
    idade: int
    sexo: str

lista_pesquisa = []

# === MENU ===
while True:
    print("""
        Código {1} = Adicionar pessoa
        Código {2} = Exibir resultados
        Código {3} = Sair
          """)
        
    codigo = int(input("Digite o código: "))

    match codigo:
        case 1:
                salario = float(input("Digite o seu salário: "))
                idade = int(input("Digite a sua idade: "))
                sexo = str(input("Digite o seu sexo(M/F): ")).upper()
                lista_pesquisa.append(Dados(salario=salario, idade=idade, sexo=sexo))
                
                continuar = input("Deseja adicionar outra pesquisa? (sim/não): ")
                while continuar.lower() != 'sim':
                    break
        case 2:
            nome_do_arquivo = "Pesquisa.txt"
            with open(nome_do_arquivo, "w") as arquivo_alunos:
                for dado in lista_pesquisa:
                    arquivo_alunos.write(f"{dado.salario}, {dado.idade}, {dado.sexo}\n")

            salarios = [dado.salario for dado in lista_pesquisa]
            idade = [dado.idade for dado in lista_pesquisa]

            contador = len(lista_pesquisa)
            soma = sum(salarios)
            media = soma / contador
            maior = max(idade)
            menor = min(idade)
            total_mulheres = sum(1 for dado in lista_pesquisa if dado.sexo == "F" and dado.salario == 5000)

            print(" === RESULTADOS === ")
            print(f"Total da pesquisa: {contador}")
            print(f"idade maior: {maior}, idade menor: {menor}")
            print(f"Soma do salário: {soma}")
            print(f"Média do salário: {media}")
            print(f"Quantidade de mulheres com salário de R$5.000: {total_mulheres}")
        case 3:
            print("Saindo do sistema")
            break
        case _:
            print("Opção inválida.")