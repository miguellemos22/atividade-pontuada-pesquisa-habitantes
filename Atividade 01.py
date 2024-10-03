import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Dados:
    salario: float
    filhos: int

lista_pesquisa = []

# === MENU ===
while True:
    print("""
        Código {1} = Adicionar família
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
                filhos = int(input("Digite a quantidade de filhos que você tem: "))
                lista_pesquisa.append(Dados(salario=salario, filhos=filhos))
        case 2:
            nome_do_arquivo = "Pesquisa_prefeitura.txt"
            with open(nome_do_arquivo, "a") as arquivo_alunos:
                for dado in lista_pesquisa:
                    arquivo_alunos.write(f"{dado.salario}, {dado.filhos}\n")

            salarios = [dado.salario for dado in lista_pesquisa]
            filhos_total = sum(dado.filhos for dado in lista_pesquisa)

            contador = len(lista_pesquisa)
            soma = sum(salarios)
            media = soma / contador
            maior = max(salarios)
            menor = min(salarios)

            print(" === RESULTADOS === ")
            print(f"Total de famílias que responderam: {contador}")
            print(f"Salário maior: {maior}, salário menor: {menor}")
            print(f"Soma do salário: {soma}")
            print(f"Média do salário: {media}")
            print(f"Nº total de filhos: {filhos_total}")

        case 3:
            print("Saindo do sistema")
            break
        case _:
            print("Opção inválida.")