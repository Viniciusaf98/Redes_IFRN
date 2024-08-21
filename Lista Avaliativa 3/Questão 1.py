import random
import sys

try:
    listas = int(input("Informe a quantidade de listas que a matriz terá : "))
    elementos = int(input("Informe a quantidade de elementos em cada lista : "))
except ValueError:
    print("Erro! Você deve informar números inteiros.")
    sys.exit()

if listas <= 0 or elementos <= 0:
    print("Erro! A quantidade de listas e elementos deve ser positiva.")
    sys.exit()

matriz = [[random.randint(0, 100) for _ in range(elementos)] for _ in range(listas)]

print("Matriz Original : ")
for linha in matriz:
    print(linha)

matriz_transposta = [[matriz[j][i] for j in range(listas)] for i in range(elementos)]

print("Matriz Transposta : ")
for linha in matriz_transposta:
    print(linha)
