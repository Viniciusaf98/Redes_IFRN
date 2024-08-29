file_name = "alunos_ifrn.csv"  # Nome fixo do arquivo conforme a questão

# Abrir e ler o arquivo
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Inicializar variáveis
campus_counts = {}
ano_counts = {}
curso_counts = {}

total_alunos = 0

# Processar as linhas do arquivo
for line in lines:
    parts = line.strip().split(';')
    if len(parts) >= 8:
        campus = parts[7].strip()
        ano = parts[5][:4].strip()
        curso = parts[4].strip()
        
        # Contagem por campus
        if campus:
            if campus not in campus_counts:
                campus_counts[campus] = 0
            campus_counts[campus] += 1
        
        # Contagem por ano
        if ano:
            if ano not in ano_counts:
                ano_counts[ano] = 0
            ano_counts[ano] += 1
        
        # Contagem por curso (para o campus escolhido mais tarde)
        if curso and campus:
            if campus not in curso_counts:
                curso_counts[campus] = {}
            if curso not in curso_counts[campus]:
                curso_counts[campus][curso] = 0
            curso_counts[campus][curso] += 1
        
        total_alunos += 1

# Montar lista para campus
campus_list = []
for campus, count in campus_counts.items():
    percentual = (count / total_alunos) * 100
    campus_list.append([campus, count, round(percentual, 2)])

# Salvar a lista de campus em um arquivo
with open('alunos_ifrn_campus.csv', 'w', encoding='utf-8') as file:
    for item in campus_list:
        file.write(f"{item[0]};{item[1]};{item[2]}\n")

# Montar lista para ano de ingresso
ano_list = []
for ano, count in ano_counts.items():
    ano_list.append([ano, count])

# Salvar a lista de anos em um arquivo
with open('alunos_ifrn_ano.csv', 'w', encoding='utf-8') as file:
    for item in ano_list:
        file.write(f"{item[0]};{item[1]}\n")

# Listar campus e pedir escolha do usuário
print("Campi disponíveis:")
for campus in campus_counts.keys():
    print(campus)
    
escolha = input("Escolha um campus: ").strip()

# Verificar se a escolha é válida
if escolha in curso_counts:
    # Montar lista para cursos no campus escolhido
    curso_list = []
    for curso, count in curso_counts[escolha].items():
        curso_list.append([curso, count])

    # Salvar a lista de cursos em um arquivo
    with open('alunos_ifrn_campus_curso.csv', 'w', encoding='utf-8') as file:
        for item in curso_list:
            file.write(f"{item[0]};{item[1]}\n")
else:
    print("Campus escolhido não é válido.")
