import random
import math

n = int(input("Digite um valor para n (entre 7 e 60) : "))
while n < 7 or n > 60:
    n = int(input("Valor inválido. Digite um valor para n (entre 7 e 60) : "))

# Gera a lista de números aleatórios
numeros = random.sample(range(1, 61), n)

# Cria uma lista com todas as combinações possíveis
combinações = []
numeros.sort()

for i in range(len(numeros) - 5):
    for j in range(i + 1, len(numeros) - 4):
        for k in range(j + 1, len(numeros) - 3):
            for l in range(k + 1, len(numeros) - 2):
                for m in range(l + 1, len(numeros) - 1):
                    for o in range(m + 1, len(numeros)):
                        combinações.append([numeros[i], numeros[j], numeros[k], numeros[l], numeros[m], numeros[o]])

# Salva a lista de números escolhidos em um arquivo.txt
with open("numeros_escolhidos.txt", "w") as file:
    file.write(";".join(map(str, numeros)))

# Salva as combinações em um arquivo.txt
with open("combinacoes.txt", "w") as file:
    for combinacao in combinações:
        file.write(";".join(map(str, combinacao)) + "\n")

# Exibe o número de combinações e calcula as probabilidades
total_combinacoes = len(combinações)
print(f"Total de combinações geradas: {total_combinacoes}")

# Cálculo das probabilidades baseado na lista gerada
total_possibilidades = math.comb(n, 6)
prob_sena = 1 / total_possibilidades
prob_quina = 1 / math.comb(n, 5)
prob_quadra = 1 / math.comb(n, 4)

print(f"Probabilidade de acertar a Sena: 1 em {total_possibilidades} ({prob_sena:.10f})")
print(f"Probabilidade de acertar a Quina: 1 em {math.comb(n, 5)} ({prob_quina:.10f})")
print(f"Probabilidade de acertar a Quadra: 1 em {math.comb(n, 4)} ({prob_quadra:.10f})")
