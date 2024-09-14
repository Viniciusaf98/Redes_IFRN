import requests
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime
from tabulate import tabulate

ano_atual = datetime.now().year

while True:
    ano_informado = input(f"Informe o ano desejado (entre 1985 e {ano_atual}): ")
    if ano_informado.isdigit() and 1985 <= int(ano_informado) <= ano_atual:
        ano_informado = int(ano_informado)
        break
    else:
        print(f"O ano que deve ser informado é entre 1985 e {ano_atual}.")

# URL da API para obter as moedas disponíveis
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'

# Tenta acessar a API e obter as moedas disponíveis
try:
    response = requests.get(strURL)
    response.raise_for_status()
    dictMoedas = response.json()
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")
    exit()
except ValueError as e:
    print(f"Erro ao interpretar a resposta da API como JSON: {e}")
    exit()

# Cria e exibe tabela com as moedas disponíveis
moedas_disponiveis = [(moeda['simbolo'], moeda['nomeFormatado']) for moeda in dictMoedas.get('value', [])]
if not moedas_disponiveis:
    print("Nenhuma moeda foi encontrada na API.")
    exit()

tabela_moedas = tabulate(moedas_disponiveis, headers=["Sigla", "Nome da Moeda"], tablefmt="grid")

print("\nMoedas Disponíveis:")
print(tabela_moedas)

# Solicita ao usuário que informe uma moeda válida
while True:
    moeda_informada = input("Informe a moeda desejada (use a sigla): ").upper()
    if any(moeda_informada == moeda['simbolo'] for moeda in dictMoedas['value']):
        break
    else:
        print("Moeda inválida. Por favor, escolha uma moeda da tabela acima.")

# Monta a URL da API para obter as cotações da moeda informada no ano especificado
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27{moeda_informada}%27&@dataInicial=%2701-01-{ano_informado}%27&'
strURL += f'@dataFinalCotacao=%2712-31-{ano_informado}%27&$format=json'

# Tenta acessar a API e obter as cotações
try:
    response = requests.get(strURL)
    response.raise_for_status()
    dictCotacoes = response.json()
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")
    print("Por favor, tente novamente com outro ano ou moeda.")
    exit()
except ValueError as e:
    print(f"Erro ao interpretar a resposta da API como JSON: {e}")
    exit()

# Verifica se a resposta contém dados válidos
if not dictCotacoes.get('value'):
    print("Não há dados disponíveis para a moeda e o ano informados.")
    exit()

# Calcula as médias mensais de compra e venda
medias = {}
for cotacao in dictCotacoes['value']:
    try:
        data = cotacao['dataHoraCotacao'].split('T')[0]
        mes = data[5:7]
        if mes not in medias:
            medias[mes] = {'mediaCompra': [], 'mediaVenda': []}
        if cotacao['cotacaoCompra'] is not None and cotacao['cotacaoVenda'] is not None:
            medias[mes]['mediaCompra'].append(float(cotacao['cotacaoCompra']))
            medias[mes]['mediaVenda'].append(float(cotacao['cotacaoVenda']))
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar dados de cotação: {e}")
        continue

# Calcula as médias para cada mês e arredonda para 5 casas decimais
medias_calculadas = {}
for mes in medias:
    if medias[mes]['mediaCompra'] and medias[mes]['mediaVenda']:
        mediaCompra = sum(medias[mes]['mediaCompra']) / len(medias[mes]['mediaCompra'])
        mediaVenda = sum(medias[mes]['mediaVenda']) / len(medias[mes]['mediaVenda'])
        medias_calculadas[mes] = {
            'mediaCompra': round(mediaCompra, 5),
            'mediaVenda': round(mediaVenda, 5)
        }

# Nome dos arquivos
nome_arquivo_json = f'medias_cotacoes_{moeda_informada}_{ano_informado}.json'
nome_arquivo_csv = f'medias_cotacoes_{moeda_informada}_{ano_informado}.csv'

# Verifica se os arquivos já existem e avisa o usuário
if os.path.exists(nome_arquivo_json):
    print(f"Atenção: O arquivo {nome_arquivo_json} já existe e será sobrescrito.")
if os.path.exists(nome_arquivo_csv):
    print(f"Atenção: O arquivo {nome_arquivo_csv} já existe e será sobrescrito.")

# Salva as médias em um arquivo JSON
try:
    with open(nome_arquivo_json, 'w') as json_file:
        json.dump(medias_calculadas, json_file, indent=4)
except IOError as e:
    print(f"Erro ao salvar o arquivo JSON: {e}")
    exit()

# Salva as médias em um arquivo CSV
try:
    with open(nome_arquivo_csv, 'w') as csv_file:
        csv_file.write('moeda;mes;mediaCompra;mediaVenda\n')
        for mes in medias_calculadas:
            csv_file.write(f'{moeda_informada};{mes};{medias_calculadas[mes]["mediaCompra"]};{medias_calculadas[mes]["mediaVenda"]}\n')
except IOError as e:
    print(f"Erro ao salvar o arquivo CSV: {e}")
    exit()

print("Processo concluído com sucesso.")


# Exibe um gráfico de linha com as médias de compra e venda ao longo dos meses (Caso apareça apenas uma linha, recomendo utilizar o zoom pois os números são bem próximos)
meses = sorted(medias_calculadas.keys())
mediaCompra = [medias_calculadas[mes]['mediaCompra'] for mes in meses]
mediaVenda = [medias_calculadas[mes]['mediaVenda'] for mes in meses]

plt.figure(figsize=(10, 5))
plt.plot(meses, mediaCompra, label='Média Compra', marker='o')
plt.plot(meses, mediaVenda, label='Média Venda', marker='o')
plt.title(f'Média Cotações {moeda_informada} – Ano {ano_informado}')
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

print("Processo concluído com sucesso.")
