import os

arquivos = ["CotacoesDolar2023.csv", "CotacoesDolar2024.csv"]

for file_name in arquivos:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        # Inicializar acumuladores para cada mês
        cotacoes = [[float('-inf'), '', 0, 0] for _ in range(12)]  

        for line in lines:
            parts = line.strip().split(';')
            if len(parts) >= 6:
                date = parts[0]
                venda = float(parts[5].replace(',', '.'))
                month = int(date[3:5]) - 1

                cotacoes[month] = [
                    max(cotacoes[month][0], venda), 
                    date if venda > cotacoes[month][0] else cotacoes[month][1],
                    cotacoes[month][2] + venda, 
                    cotacoes[month][3] + 1
                ]

        # Criação das listas usando List Comprehensions e MAP
        max_cotacoes = [[meses[i], round(cotacao[0], 2), cotacao[1]] for i, cotacao in enumerate(cotacoes) if cotacao[3] > 0]
        media_cotacoes = [[meses[i], round(cotacao[2] / cotacao[3], 2)] for i, cotacao in enumerate(cotacoes) if cotacao[3] > 0]

        # Ordenar as listas (já estão ordenadas por mês devido ao índice, mas aqui apenas por segurança)
        max_cotacoes.sort(key=lambda x: meses.index(x[0]))
        media_cotacoes.sort(key=lambda x: meses.index(x[0]))

        print(f"Resultados para {file_name}:")
        print("Maior cotação e data por mês:")
        for item in max_cotacoes:
            print(f"Mês: {item[0]}, Maior Cotação: {item[1]}, Data: {item[2]}")

        print("\nMédia das cotações por mês:")
        for item in media_cotacoes:
            print(f"Mês: {item[0]}, Média: {item[1]}")
        print("\n" + "-"*40 + "\n")
    else:
        print(f"Arquivo {file_name} não encontrado.")