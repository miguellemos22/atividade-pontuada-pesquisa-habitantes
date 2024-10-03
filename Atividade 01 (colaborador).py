import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Dados:
    salario: float
    idade: int
    sexo: int

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
            continuar = input("Deseja adicionar uma família? (sim/não): ")
            while continuar.lower() == 'sim':
                salario = float(input("Digite o seu salário: "))
                continuar = input("Deseja adicionar outra família? (sim/não): ")
                idade = int(input("Digite a quantidade de filhos que você tem: "))
                sexo = int(input("Digite o seu sexo(M/F): "))
                lista_pesquisa.append(Dados(salario=salario, idade=idade, sexo=sexo))
        case 2:
            nome_do_arquivo = "Pesquisa_prefeitura.txt"
            with open(nome_do_arquivo, "a") as arquivo_alunos:
                for dado in lista_pesquisa:
                    arquivo_alunos.write(f"{dado.salario}, {dado.idade}, {dado.sexo}\n")

            salarios = [dado.salario for dado in lista_pesquisa]
            idade_total = sum(dado.idade for dado in lista_pesquisa)

            contador = len(lista_pesquisa)
            soma = sum(salarios)
            media = soma / contador
            maior = max(idade)
            menor = min(idade)

            print(" === RESULTADOS === ")
            print(f"Total de famílias que responderam: {contador}")
            print(f"Salário maior: {maior}, salário menor: {menor}")
            print(f"Soma do salário: {soma}")
            print(f"Média do salário: {media}")
            print(f"Nº total de filhos: {idade_total}")

        case 3:
            print("Saindo do sistema")
            break
        case _:
            print("Opção inválida.")