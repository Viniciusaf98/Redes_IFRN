import subprocess

host = input("Digite o nome de uma máquina de destino (HOST): ")

# Realiza o rastreamento e salva a resposta em um arquivo
strCMD = f'tracert -d4 {host}'
caminho = subprocess.run(strCMD, capture_output=True).stdout.decode('latin1')

with open('rastreamento.txt', 'w', encoding='latin1') as arquivo:
    arquivo.write(caminho)

# Indica o menor tempo em que cada uma das máquinas no caminho foi atingida
linhas = caminho.split('\r\n')
tempos = []

for linha in linhas:
    partes = linha.split()
    ms_list = [p for p in partes if 'ms' in p.lower()]

    if ms_list:
        tempos_ms = [int(ms.replace('ms', '').replace('<', '').strip()) for ms in ms_list if ms.replace('ms', '').replace('<', '').strip().isdigit()]
        if tempos_ms:
            menor_tempo = min(tempos_ms)
            tempos.append(menor_tempo)

if tempos:
    print("Menores tempos em ms para cada salto:")
    for tempo in tempos:
        print(tempo, "ms")
else:
    print("Nenhum tempo foi identificado nos resultados.")
