import requests
import json
from datetime import datetime
from tabulate import tabulate 

ano_atual = datetime.now().year

# Solicita o ano desejado ao usuário e valida a entrada
try:
    ano_informado = int(input(f"Informe o ano (2021 a {ano_atual}): "))
except ValueError:
    print("Erro: O ano informado deve ser um número inteiro.")
    exit()

while ano_informado < 2021 or ano_informado > ano_atual:
    try:
        ano_informado = int(input(f"Ano inválido. Informe um ano entre 2021 e {ano_atual}: "))
    except ValueError:
        print("Erro: O ano informado deve ser um número inteiro.")
        exit()

# Carrega os dados de acordo com o ano informado
try:
    if ano_informado == ano_atual:
        strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
        dictCartola = requests.get(strURL).json()
    else:
        nome_arquivo = f'cartola_fc_{ano_informado}.json'
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            dictCartola = json.load(file)
except requests.exceptions.RequestException as e:
    print("Erro ao fazer a requisição:", e)
    exit()
except FileNotFoundError:
    print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    exit()
except json.JSONDecodeError:
    print(f"Erro ao decodificar o arquivo {nome_arquivo}.")
    exit()
except UnicodeDecodeError:
    print(f"Erro ao decodificar o arquivo {nome_arquivo} devido à codificação incorreta.")
    exit()

# Lista de esquemas táticos disponíveis
escalacao_disponiveis = {
    1: '3-4-3',
    2: '3-5-2',
    3: '4-3-3',
    4: '4-4-2',
    5: '4-5-1',
    6: '5-3-2',
    7: '5-4-1'
}

# Exibe as opções de esquemas táticos em uma tabela
print("Escolha uma das escalações que estão disponíveis :")
tabela_escalacoes = [[num, escalacao] for num, escalacao in escalacao_disponiveis.items()]
print(tabulate(tabela_escalacoes, headers=['Número', 'Escalação'], tablefmt='grid'))

# Solicita o esquema tático desejado e valida a entrada
try:
    escalacao_escolhida = int(input("Informe o numero (1 a 7) da escalação que você deseja escolher : "))
except ValueError:
    print("Erro: A escolha deve ser um número inteiro.")
    exit()

while escalacao_escolhida < 1 or escalacao_escolhida > 7:
    try:
        escalacao_escolhida = int(input("Escalação invalida. Escolha uma escalação dentre as apresentadas : "))
    except ValueError:
        print("Erro: A escolha deve ser um número inteiro.")
        exit()

# Definindo as posições e quantidades de jogadores por posição para cada esquema tático
esquemas_taticos = {
    '3-4-3': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 4, 'atacante': 3, 'tecnico': 1},
    '3-5-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 5, 'atacante': 2, 'tecnico': 1},
    '4-3-3': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 3, 'atacante': 3, 'tecnico': 1},
    '4-4-2': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 4, 'atacante': 2, 'tecnico': 1},
    '4-5-1': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 5, 'atacante': 1, 'tecnico': 1},
    '5-3-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 3, 'atacante': 2, 'tecnico': 1},
    '5-4-1': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 4, 'atacante': 1, 'tecnico': 1},
}

# Escolha do esquema tático
esquema_selecionado = escalacao_disponiveis[escalacao_escolhida]
quantidade_posicoes = esquemas_taticos[esquema_selecionado]

# Selecionando os jogadores com as maiores pontuações em cada posição
selecionados = {}

for posicao, quantidade in quantidade_posicoes.items():
    posicao_id = {
        'goleiro': 1,
        'zagueiro': 3,
        'lateral': 2,
        'meia': 4,
        'atacante': 5,
        'tecnico': 6
    }[posicao]
    
    jogadores = [atleta for atleta in dictCartola['atletas'] if atleta['posicao_id'] == posicao_id]
    
    # Calcula a pontuação total (média de pontos x quantidade de partidas)
    for atleta in jogadores:
        atleta['pontuacao_total'] = round(atleta.get('media_num', 0) * atleta.get('jogos_num', 0), 2)
    
    # Ordena os jogadores pela pontuação total e seleciona os melhores
    jogadores = sorted(jogadores, key=lambda x: x.get('pontuacao_total', 0), reverse=True)[:quantidade]
    
    selecionados[posicao] = jogadores

# Construindo o dicionário final e ajustando a URL das fotos
cartola_selecao = {}

for posicao, atletas in selecionados.items():
    for atleta in atletas:
        id_atleta = atleta['atleta_id']
        foto_url = atleta.get('foto', '')
        foto_url = foto_url.replace('_FORMATO_', '_220x220_').replace('_FORMATO', '_220x220')

        # Verificando se o clube existe no dicionário de clubes
        clube_id = str(atleta['clube_id'])
        clube_nome = dictCartola['clubes'].get(clube_id, {}).get('nome', 'Clube Desconhecido')
        escudo_url = dictCartola['clubes'].get(clube_id, {}).get('escudos', {}).get('60x60', '')

        cartola_selecao[id_atleta] = {
            'id': id_atleta,
            'nome': atleta.get('nome', 'Desconhecido'),
            'apelido': atleta.get('apelido', 'Sem Apelido'),
            'url_foto': foto_url,
            'clube': clube_nome,
            'escudo': escudo_url,
            'id_posicao': atleta['posicao_id'],
            'nome_posicao': posicao,
            'pontuacao': atleta.get('pontuacao_total', 0)
        }

# Salvando o dicionário em JSON
try:
    with open(f'cartola_selecao_{esquema_selecionado}_{ano_informado}.json', 'w', encoding='utf-8') as outfile:
        json.dump(cartola_selecao, outfile, indent=4, ensure_ascii=False, )
except IOError:
    print("Erro ao salvar o arquivo JSON.")
    exit()

# Exibindo a seleção final em uma tabela
print("\nSeleção do Cartola FC:")
tabela_selecao = []
for posicao in ['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'tecnico']:
    if posicao in selecionados:
        for atleta in selecionados[posicao]:
            clube_id = str(atleta['clube_id'])
            clube_nome = dictCartola['clubes'].get(clube_id, {}).get('nome', 'Clube Desconhecido')
            tabela_selecao.append([
                atleta['nome'],
                atleta['apelido'],
                clube_nome,
                posicao.capitalize(),
                f"{atleta.get('pontuacao_total', 0):.2f}"
            ])

print(tabulate(tabela_selecao, headers=['Nome', 'Apelido', 'Clube', 'Posição', 'Pontuação'], tablefmt='grid'))
