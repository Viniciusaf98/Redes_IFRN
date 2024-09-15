import random
from tabulate import tabulate

# Função para gerar cartelas
def gerarCartelas(n):
    if n <= 0 or n > 10000:
        return False, "\nErro: O número de cartelas deve ser positivo e no máximo 10.000."
    
    cartelas = {}
    cartela_ids = set()
    
    for _ in range(n):
        while True:
            numero_cartela = f"CART_{random.randint(1, 100000):06}"
            if numero_cartela not in cartela_ids:
                cartela_ids.add(numero_cartela)
                break

        cartela = {
            'B': sorted(random.sample(range(1, 15), 5)),
            'I': sorted(random.sample(range(16, 30), 5)),
            'N': sorted(random.sample(range(31, 45), 5)),
            'G': sorted(random.sample(range(46, 60), 5)),
            'O': sorted(random.sample(range(61, 75), 5))
        }

        cartelas[numero_cartela] = cartela

    return True, cartelas

# Função para salvar cartelas
def salvarCartelas(cartelas, nome_arquivo="cartelas.txt"):
    if not cartelas:
        return False, "\nErro: Nenhuma cartela para salvar."

    try:
        with open(nome_arquivo, 'w') as file:
            for numero_cartela, cartela in cartelas.items():
                linha = f"{numero_cartela};" + ";".join(
                    [",".join(map(str, cartela[letra])) for letra in ['B', 'I', 'N', 'G', 'O']]
                )
                file.write(linha + "\n")
        return True, "\nArquivo salvo com sucesso."
    except Exception as e:
        return False, f"\nErro ao salvar o arquivo: {str(e)}"

# Função para ler cartelas
def lerCartelas(nome_arquivo="cartelas.txt"):
    try:
        with open(nome_arquivo, 'r') as file:
            cartelas = {}
            for linha in file:
                partes = linha.strip().split(';')
                numero_cartela = partes[0]
                cartela = {
                    'B': list(map(int, partes[1].split(','))),
                    'I': list(map(int, partes[2].split(','))),
                    'N': list(map(int, partes[3].split(','))),
                    'G': list(map(int, partes[4].split(','))),
                    'O': list(map(int, partes[5].split(',')))
                }
                cartelas[numero_cartela] = cartela
        return True, cartelas
    except FileNotFoundError:
        return False, "\nErro: Arquivo não encontrado."
    except Exception as e:
        return False, f"\nErro ao ler o arquivo: {str(e)}"

# Função para imprimir uma cartela
def imprimirCartelas(cartelas):
    if not cartelas:
        return False, "\nErro: Nenhuma cartela foi gerada."

    while True:
        n = input("\nInforme o número da cartela (6 dígitos) ou digite 0 para sair: ")
        if n == "0":
            return False, "\nSaída solicitada."
        elif f"CART_{n.zfill(6)}" in cartelas:
            cartela = cartelas[f"CART_{n.zfill(6)}"]

            tabela = [
                ['B', 'I', 'N', 'G', 'O'],
                [cartela['B'][0], cartela['I'][0], cartela['N'][0], cartela['G'][0], cartela['O'][0]],
                [cartela['B'][1], cartela['I'][1], cartela['N'][1], cartela['G'][1], cartela['O'][1]],
                [cartela['B'][2], cartela['I'][2], cartela['N'][2], cartela['G'][2], cartela['O'][2]],
                [cartela['B'][3], cartela['I'][3], cartela['N'][3], cartela['G'][3], cartela['O'][3]],
                [cartela['B'][4], cartela['I'][4], cartela['N'][4], cartela['G'][4], cartela['O'][4]]
            ]

            print(f"\nCartela : {n.zfill(6)}")
            resultado = tabulate(tabela, headers='firstrow', tablefmt="grid")
            print(resultado)
            return True, resultado
        else:
            print("\nErro: Número de cartela inválido, tente novamente.")

# Função para sortear dezenas
def sortearDezenas(cartelas):
    dezenas_sorteadas = random.sample(range(1, 76), 25)
    print(f"\nDezenas sorteadas: {dezenas_sorteadas}")

    while True:
        cartelas_batidas = []
        for numero_cartela, cartela in cartelas.items():
            numeros_cartela = cartela['B'] + cartela['I'] + cartela['N'] + cartela['G'] + cartela['O']
            if all(numero in dezenas_sorteadas for numero in numeros_cartela):
                numero_cartela_batida = numero_cartela.split('_')[1]
                cartelas_batidas.append(numero_cartela_batida)

        if cartelas_batidas:
            print("\nCartelas batidas:")
            tabela_cartelas = [[num.center(6)] for num in cartelas_batidas]
            print(tabulate(tabela_cartelas, headers=['Número da Cartela'], tablefmt="grid"))
            break
        else:
            nova_dezena = random.choice([x for x in range(1, 76) if x not in dezenas_sorteadas])
            dezenas_sorteadas.append(nova_dezena)
            print(f"\nNova dezena sorteada: {nova_dezena}")

    print(f"\nDezenas sorteadas: {dezenas_sorteadas}")

# Função principal do programa (Menu)
def menu():
    cartelas_geradas = {}

    while True:
        print(tabulate([['1', 'Gerar Cartelas'],
                        ['2', 'Salvar Cartelas'],
                        ['3', 'Ler Cartelas'],
                        ['4', 'Imprimir Cartelas'],
                        ['5', 'Sortear Dezenas'],
                        ['6', 'Sair']], headers=['Opção', 'Descrição'], tablefmt="grid"))

        opcao = input("\nEscolha uma opção dentre as oferecidas : ")

        if opcao == "1":
            while True:
                try:
                    n = int(input("\nQuantas cartelas você deseja gerar? (máximo 10.000) : "))
                    if n > 0 and n <= 10000:
                        break
                    else:
                        print("\nErro: Informe um número válido entre 1 e 10.000.")
                except ValueError:
                    print("\nErro: Informe um número válido entre 1 e 10.000.")
            sucesso, resultado = gerarCartelas(n)
            if sucesso:
                cartelas_geradas = resultado
                if n == 1:
                    print(f"\n{n} cartela foi gerada com sucesso.")
                else:
                    print(f"\n{n} Cartelas foram geradas com sucesso.")
            else:
                print(resultado)
        
        elif opcao == "2":
            sucesso, mensagem = salvarCartelas(cartelas_geradas)
            print(mensagem)
        
        elif opcao == "3":
            nome_arquivo = "cartelas.txt"
            sucesso, resultado = lerCartelas(nome_arquivo)
            if sucesso:
                cartelas_geradas = resultado
                print("\nCartelas lidas com sucesso.")
            else:
                print(resultado)

        elif opcao == "4":
            if cartelas_geradas:
                imprimirCartelas(cartelas_geradas)
            else:
                print("\nErro: Nenhuma cartela foi gerada.")
        
        elif opcao == "5":
            if cartelas_geradas:
                sortearDezenas(cartelas_geradas)
            else:
                print("\nErro: Nenhuma cartela foi gerada.")

        elif opcao == "6":
            print("\nSaindo do programa.")
            break

        else:
            print("\nOpção inválida. Tente novamente digitando um número de 1 a 6.")

if __name__ == "__main__":
    menu()
