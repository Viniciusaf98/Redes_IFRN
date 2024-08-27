import random
import sys

listas = input("Informe a quantidade de listas que a matriz terá: ")
elementos = input("Informe a quantidade de elementos em cada lista: ")

    # Verifica se ambas as entradas são números inteiros e positivos
if listas.isdigit() and elementos.isdigit():
    listas = int(listas)
    elementos = int(elementos)
else:
    print("Erro! Você deve informar números inteiros e positivos.")
    sys.exit()


    # Cria a matriz com números aleatórios entre 0 e 100
matriz = [[random.randint(0, 100) for _ in range(elementos)] for _ in range(listas)]

    # Exibe a matriz original
print("Matriz Original:")
for linha in matriz:
    print(linha)

    # Calcula a matriz transposta
matriz_transposta = [[matriz[j][i] for j in range(listas)] for i in range(elementos)]

print("Matriz Transposta:")
for linha in matriz_transposta:
    print(linha)
