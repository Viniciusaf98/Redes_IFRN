gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']
lista_alunos = [ 
    ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A']
]

lista_alunos_resultado = []

    # Calculando os acertos de cada aluno e adicionando na lista de resultados
for alunos in lista_alunos:
    nome = alunos[0]
    respostas = alunos[1:]
    acertos = sum(1 for i in range(len(gabarito)) if respostas[i] == gabarito[i])
    lista_alunos_resultado.append([nome, acertos, respostas])

    # Ordenando a lista de alunos pelo número de acertos em ordem decrescente
lista_alunos_resultado.sort(key=lambda x: x[1], reverse=True)

    # Exibindo os resultados
print("Gabarito:", " ".join(gabarito))
print()
for aluno in lista_alunos_resultado:
    nome, acertos, respostas = aluno
    print(f"Nome: {nome}")
    print(f"Respostas: {' '.join(respostas)}")
    print(f"O número de acertos: {acertos}")
    print()
